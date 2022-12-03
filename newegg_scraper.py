import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests
import os

"""

response = requests.get("https://www.newegg.com/robots.txt")
robots_txt = response.text
print("robots.txt for Newegg.com")
print("===================================================")
print(robots_txt)
print("=================END robots.txt====================")

"""
search_product = input('Search for a product on Newegg: ').replace(" ", "+")
search_url = 'https://www.newegg.com/p/pl?d='
url = search_url + search_product

page = urlopen(url)
page_html = page.read()
page.close()

file_path = input("Please enter a file path that you would like to use for output file: ")

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-container"})

# Save the output product_s.csv file to the user-specified directory
filename_output = f"{file_path}/CSVoutput/product_result.csv"
os.makedirs(os.path.dirname(filename_output), exist_ok=True)
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
