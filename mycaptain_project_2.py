#Web Scraper using BeautifulSoup4 and requests
import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090"

req= requests.get(url)
content = req.content


soup = BeautifulSoup(content,"html.parser")

name=soup.find_all("h1",attrs={'class': "product-title"})[0].get_text()

price = soup.find_all("div", attrs={'class': "price-current"})[0].get_text()

print("Current price of "+name+" is: "+price)