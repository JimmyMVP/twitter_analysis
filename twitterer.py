

API_KEY = "ZpMiVjbhAK9rHVFY34JfPy8Or"

import tweepy
from tweepy import OAuthHandler
import os 


 
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET']
access_token = os.environ['TWITTER_TOKEN_KEY']
access_secret = os.environ['TWITTER_TOKEN_SECRET']
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)