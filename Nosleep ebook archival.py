#A quick script to scrape several ebooks at once from "nosleepbook.wordpress.com" for purposes of archival
from bs4 import  BeautifulSoup
import requests

ebook = requests.get("https://nosleepebook.wordpress.com/2017/03/").text
soup = BeautifulSoup(ebook, "lxml")
links = soup.find_all("option")
links.pop(0) #to remove the page already selected page from the list because it has no books to download
#print(links)
dict_of_files = dict()

#Creating a dictionary with the release date of the book as the key to be used as title, and the link as value.
for element in links:
    x = str(element)
    if '<option selected="selected" value="' in x:
        x = x.replace('<option selected="selected" value="'," ")
    elif '<option value="' in x:
        x = x.replace('<option value="', " ")
    x = x.replace('">',"")
    x = x.replace('</option>',"")
    x = x.strip()
    x = x.partition(" ")
    #print(x)
    dict_of_files[x[2]] = x[0]
    #print(dict_of_files)
del dict_of_files["March 2017"]

#Need to go to each link specified in the dictionary as a value and download the book
for key,value in dict_of_files.items():
    newbook = requests.get(value).text
