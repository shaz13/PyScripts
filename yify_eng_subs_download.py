import requests
from bs4 import BeautifulSoup

query = raw_input('Enter the string: ')
url = "http://www.yifysubtitles.com/search?q=" + str(query)
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

mydivs = soup.findAll("ul", { "class" : "media-list" })


for i in mydivs:
	print i