# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup
import csv
import re

def cnn_scrape():
    url = 'https://edition.cnn.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headline_text = []
    for headline in soup.find_all(class_="container__headline-text"):
        # Get the text of the headline
        text = headline.get_text(strip=True)
        # Check if the headline has more than 4 words
        if len(text.split()) > 4:
            headline_text.append(text)
    
    # Print the final list of headlines
    print(headline_text)

    # Write to CSV file
    with open('CNN_scrape.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each headline as a new row
        for headline in headline_text:
            writer.writerow([headline])

if __name__ == '__main__':
    cnn_scrape()

def bbc_scrape():
    url = 'https://www.bbc.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headline_text = []
    for headline in soup.find_all(class_="sc-9d830f2a-3 fWzToZ"):
        # Get the text of the headline
        text = headline.get_text(strip=True)
        headline_text.append(text)
    
    # Print the final list of headlines
    print(headline_text)

    # Write to CSV file
    with open('BBC_scrape.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each headline as a new row
        for headline in headline_text:
            writer.writerow([headline])

if __name__ == '__main__':
    bbc_scrape()

def apnews_scrape():
    url = 'https://apnews.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headline_text = []
    for headline in soup.find_all(class_="PagePromoContentIcons-text"):
        # Get the text of the headline
        text = headline.get_text(strip=True)
        if len(text.split()) > 4:
            headline_text.append(text)
    
    # Print the final list of headlines
    print(headline_text)

    # Write to CSV file
    with open('AP_scrape.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each headline as a new row
        for headline in headline_text:
            writer.writerow([headline])

if __name__ == '__main__':
    apnews_scrape()

def npr_scrape():
    url = 'https://www.npr.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headline_text = []
    for headline in soup.find_all(class_="title"):
        # Get the text of the headline
        text = headline.get_text(strip=True)
        headline_text.append(text)
    
    # Print the final list of headlines
    print(headline_text)

    # Write to CSV file
    with open('NPR_scrape.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each headline as a new row
        for headline in headline_text:
            writer.writerow([headline])

if __name__ == '__main__':
    npr_scrape()

def buzzfeed_scrape():
    url = 'https://www.buzzfeed.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headline_text = []
    for headline in soup.find_all(class_='splashCard_heading__EzXmj'):
        # Get the text of the headline
        text = headline.get_text(strip=True)
        headline_text.append(text)
    
    # Print the final list of headlines
    print(headline_text)

    # Write to CSV file
    with open('Buzzfeed_scrape.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each headline as a new row
        for headline in headline_text:
            writer.writerow([headline])

if __name__ == '__main__':
    buzzfeed_scrape()