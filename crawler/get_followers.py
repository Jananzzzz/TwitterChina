import tweepy
import pandas as pd 
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']


auth = tweepy.AppAuthHandler(api_key, api_key_secret)
api = tweepy.API(auth=auth, wait_on_rate_limit=True)

me = api.get_user(screen_name= "@fananshi")    # need elevated access:< 

print(me)