import requests
from bs4 import BeautifulSoup

# Replace the url with your custom url
page = requests.get("https://yts.ag/")
soup = BeautifulSoup(page.content, 'html.parser')
# Note that this class and 'a' tag is unique to the url you have choosen above
mydivs = soup.findAll("a", { "class" : "browse-movie-title" })

print 'I have found %s movies on YTS Today \n'% len(mydivs)
print 'Here you go...  \n'
count = 1
for movie in mydivs:
	print count,'.', movie.text, "----"*10, movie['href']
	count+=1

# Todo
# Maintain a list of already found movies and don't show them on next run
# Email Notice
