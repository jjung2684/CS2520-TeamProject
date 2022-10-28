# CS 2520 Project

import datetime
import requests as requests
from bs4 import BeautifulSoup

time = datetime.datetime.now()
current_time = time.strftime("Current date and time is %Y/%m/%d %H:%M.")
print("\n   CS 2520 Web Scraping Project    \n")
print("Hello User, ")
print(current_time)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 " \
             "Safari/537.36 "   # Needed to help servers distinguish from human users and bots; if we don't specify, no
                                # data is retrieved
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers["User-Agent"] = USER_AGENT
session.headers["Accept-Language"] = LANGUAGE
session.headers["Content-Language"] = LANGUAGE

weather_url = "https://www.google.com/search?q=weather+pomona"
weather_html = session.get(weather_url)
weather_soup = BeautifulSoup(weather_html.text, "html.parser")      # Extract html texts from the requested URL

# In the html text, find and extract tags with location, temperature and weather and save into a dict
weather_result = {"location": weather_soup.find("div", attrs={"id": "wob_loc"}).text,
                  "temp_now": weather_soup.find("span", attrs={"id": "wob_tm"}).text,
                  "weather_now": weather_soup.find("span", attrs={"id": "wob_dc"}).text}

print("\nIn {},".format(weather_result["location"]))
print("Current weather is {}".format(weather_result["weather_now"]))
print("Current temperature is {} °F.\n".format(weather_result["temp_now"]))

cpp_url = "https://www.cpp.edu/"
cpp_html = session.get(cpp_url)
cpp_soup = BeautifulSoup(cpp_html.text, "html.parser")

print("Here are current news headlines from {}:\n".format(cpp_url))

# From the cpp website html, grab the news headlines and print them
for div in cpp_soup.findAll('div', attrs={"col-lg-3 col-md-6 col-sm-12 single-card"}):
    print("     ", (div.find('h3')).text)
    print("     ", div.find('a')['href'], "\n")

