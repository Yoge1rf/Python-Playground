#A quick script to scrape several ebooks at once from "nosleepbook.wordpress.com" for purposes of archival
from bs4 import  BeautifulSoup
import requests

ebook = requests.get("https://nosleepebook.wordpress.com/2017/03/").text
soup = BeautifulSoup(ebook, "lxml")
links = soup.find_all("option")
links.pop(0) #to remove the page already selected page from the list because it has no books to download
print(links)

#taking a break because sleepy zzzzz....




