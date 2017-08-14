import requests
from bs4 import BeautifulSoup
page = requests.get("https://yts.ag/")

soup = BeautifulSoup(page.content, 'html.parser')


mydivs = soup.findAll("a", { "class" : "browse-movie-title" })


print 'I have found %s movies on YTS Today \n'% len(mydivs)
print 'Here you go...  \n'
count = 1
for movie in mydivs:
	print count,'.', movie.text, "----"*10, movie['href']
	count+=1