from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import customtkinter
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from PIL import ImageTk, Image
import requests
import os

def scrape():
    """
    response = requests.get("https://www.newegg.com/robots.txt")
    robots_txt = response.text
    print("robots.txt for Newegg.com")
    print("===================================================")
    print(robots_txt)
    print("=================END robots.txt====================")
    """

    if textbox.get() == "":
        print("No term to search.")
        return 0

    search_product = textbox.get().replace(" ", "+")
    search_url = 'https://www.newegg.com/p/pl?d='
    url = search_url + search_product

    page = urlopen(url)
    page_html = page.read()
    page.close()

    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "item-container"})

    filename_output = filedialog.asksaveasfilename(
        filetypes=[("csv file", ".csv")],
    defaultextension=".csv")
    
    if filename_output:  # User selected file
        f = open(filename_output, "w")
        headers = "Product Name, Price, Shipping Cost, Link\n"
        f.write(headers)
        for i in range(0, len(containers)):
            container = containers[i]

            # Grab tags that we want
            title_container = container.findAll("a", {"class": "item-title"})
            product_name = title_container[0].text.strip()
            price_container = container.findAll("li", {"class": "price-current"})
            product_price = price_container[0].text.strip()

            # Discard unnecessary characters
            product_priceList = product_price.split()
            for x in range(len(product_priceList)):
                if "$" in product_priceList[x]:
                    product_price = product_priceList[x]
                    break

            product_Link = container.find('a')['href']
            shipping_container = container.findAll("li", {"class": "price-ship"})

            try:
                shipping_cost = shipping_container[0].text.strip()

            except IndexError:
                shipping_cost = ""

            print(product_name)
            print(product_price)
            print(shipping_cost)
            print(product_Link)

            f.write(product_name.replace(",", "|") + "," + product_price.replace(",", "") + "," + shipping_cost.replace(",",
"") + "," + product_Link.replace(",", "") + "\n")

        f.close()
        print("\n----------Product_result.csv file saved to {}.----------".format(filename_output))
            
    else: # User cancelled the file browser window
        print("No file chosen.") 
    
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title("Newegg Scraper")
root.geometry("500x400")
root.resizable(False, False)
root.eval("tk::PlaceWindow . center")

frame = Frame(root, width = 256, height=256)
frame.pack()
frame.place(anchor="center", relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("logo.png"))
label = Label(frame, image = img, bg='#1a1a1a')
label.pack()

box = customtkinter.CTkFrame(root, corner_radius = 10)
box.pack(pady = 20)

textbox = customtkinter.CTkEntry(box, width = 300, height = 40, border_width = 1, placeholder_text = "Search for a product on Newegg...", text_color = "silver")
textbox.grid(row = 0, column = 0, padx = 10, pady = 10)

button = customtkinter.CTkButton(box, width = 80, height = 40, text = "Scrape", command = lambda: scrape())
button.grid(row = 0, column = 1, padx = 10)

root.mainloop()
