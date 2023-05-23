import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date

def get_tweets_from_user(
    user: str = 'haoel',
    n_tweets: int = 100000
) -> pd.DataFrame:
    # To Run: get_tweets_from_user('john', n_tweets=15)

    query = "from:" + str(user)
    # Created a list to append all tweet attributes(data)
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>n_tweets:
            break
        attributes_container.append([tweet.id, tweet.date, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.sourceLabel, tweet.content, tweet.links, str(tweet)])
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(attributes_container, columns=["id", "Date Created", "LikesCount", "retweetCount", "replyCount","Source of Tweet", "Text", "links", "url"])

    return tweets_df


if __name__ == "__main__":
    df = get_tweets_from_user()
    print(df)
    df.to_csv("haoel.csv")