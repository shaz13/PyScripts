import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

OBAMA_TWIITER_URL = "https://twitter.com/BarackObama"
TRUMP_TWITTER_URL = "https://twitter.com/realDonaldTrump"

OB_PAGE = requests.get(OBAMA_TWIITER_URL)
DT_PAGE = requests.get(TRUMP_TWITTER_URL)

Obama_Soup = BeautifulSoup(OB_PAGE.content, 'html.parser')
Trump_Soup = BeautifulSoup(DT_PAGE.content, 'html.parser')


Trump_tweets = Trump_Soup.findAll("div", { "class" : "js-tweet-text-container" })

Obama_tweets = Obama_Soup.findAll("div", { "class" : "js-tweet-text-container" })

Tweets_DF = pd.DataFrame(columns=['Barack Obama', 'Donald Trump'], index=None)

for obama_tweet, trump_tweet in zip(Obama_tweets,Trump_tweets):
	df2 = pd.DataFrame([[obama_tweet.text, trump_tweet.text]], columns=['Barack Obama', 'Donald Trump'])
	Tweets_DF = Tweets_DF.append(df2, ignore_index=True)

Tweets_DF.to_csv('Obama vs. Trump.csv', encoding='utf-8', columns= ['Barack Obama', 'Donald Trump'])
