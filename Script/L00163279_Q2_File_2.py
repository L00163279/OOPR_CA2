# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

"Requests Package used to send HTTP requests"
import requests

"Used BeautifulSoup for the web scraping Purposes to pull the data from the HTML"
from bs4 import BeautifulSoup

"IP address of Ubuntu"
URL = 'http://192.168.40.128'

def scrape_data():
    try:
        "send URL Request to get all encoded form data"
        response = requests.get(URL)

        "Used html.parser to parse the data from the Page in a structured format"
        apache_page_content = BeautifulSoup(response.content, "html.parser")

        get_headers(apache_page_content)
        get_count_word_apache(apache_page_content)
        get_count_word_ubuntu(apache_page_content)
    except Exception as e:
        print(e)

"function to find page titles"
def get_headers(web_response):
    print(".........The Title of Apache Page.........")
    page_title = web_response.find("title").text
    print(page_title)
    print("\n")

"Function is to find header h2 in the page"
def get_headlines(web_response):
    page_title = web_response.find_all("h2").text
    print(page_title)

"Function is to find the count of the word apache2 in the page"
def get_count_word_apache(web_response):
    print("........The count of word apache2.........")
    count = web_response.find_all( string=lambda text: "apache2" in text.lower())
    print("Apache2 appears {} times".format(len(count)))
    print("\n")

"Function is to find the word ubuntu "
def get_count_word_ubuntu(web_response):
    print(".........checking another word : 'ubuntu'............ ")
    count1 = web_response.find_all(string=lambda text: "ubuntu" in text.lower())
    print("ubuntu appears {} times".format(len(count1)))


if __name__ == '__main__':
    scrape_data()

