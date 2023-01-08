import tweepy
import config


client = tweepy.Client(bearer_token=config.bear_token)
query = "covid -is:retweet"
query0 = "covid OR covid19 is:retweet"
query1 = "covid OR covid19 -is:retweet"

response = client.search_recent_tweets(query=query, 
tweet_fields=['created_at', 'lang'], 
user_fields=['profile_image_url'],
max_results=10, expansions=['author_id'])

users = {u['id']: u for u in response.includes['users']}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        # print(tweet.id, tweet.text, tweet.lang)
        # user.description
        print(user.username, user.profile_image_url, "\n")
        


