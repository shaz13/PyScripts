import re

file = open('Urdu_words.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
string = str(raw_input ("Enter the last ending letters: "))
def Zfinder(string):
    for word in words:
        if word[-len(string):] == string:
            print word

Zfinder(string)