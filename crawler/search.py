import tweepy
import config


client = tweepy.Client(bearer_token=config.bear_token)
query = "covid -is:retweet"
query0 = "covid OR covid19 is:retweet"
query1 = "covid OR covid19 -is:retweet"

print(client.search_recent_tweets(query=query))
