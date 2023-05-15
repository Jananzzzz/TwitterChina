import tweepy
import config


client = tweepy.Client(bearer_token=config.bear_token)
query = "openai -is:retweet"

response = client.search_recent_tweets(query=query,
                                       max_results=10,
                                       tweet_fields=['created_at', 'lang'],
                                       user_fields=['profile_image_url'],
                                       expansions=['author_id'])

users = {u['id']: u for u in response.includes['users']}
                                        
counter = 0
for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        counter += 1
        print(tweet.id, tweet.created_at, tweet.lang)
        print(user.profile_image_url)
        print(f"----------------------------------------------------{counter}")

# client = tweepy.Client(bearer_token=config.bear_token)
# query = "covid -is:retweet"
# query0 = "covid OR covid19 is:retweet"
# query1 = "covid OR covid19 -is:retweet"
# query2 = "xijinping -is:retweet"
# query3 = "(from:bboczeng) until:2022-03-04 since:2022-01-01" # need elevated api access.
# query4 = "(from:bboczeng)"

# response = client.search_recent_tweets(query=query4, 
# tweet_fields=['created_at', 'lang'], 
# user_fields=['profile_image_url'],
# max_results=100, expansions=['author_id'])

# users = {u['id']: u for u in response.includes['users']}

# counter = 0

# for tweet in response.data:
#     counter += 1
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         # print(tweet.id, tweet.text, tweet.lang)
#         # user.description
#         # print(user.username, user.profile_image_url, "\n")
#         print(tweet.text)
#         print(f"########################--------------------------------------------{counter}")
        


