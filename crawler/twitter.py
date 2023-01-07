import tweepy
import configparser

# read configs
config = configparser.ConfigParser()
config.read('./config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# authentication
auth = tweepy.OAuth2AppHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

followers = tweepy.Cursor(api.get_follower_ids, id="bboczeng")
ids = []
for page in followers.pages():
    ids.append(page)

for i in ids:
    print(i)
