import requests
import mysql.connector
import pprint
import os
import json
import get_userinfo

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFFLlAEAAAAA71tnDgI6vXrQ9%2BGnMKuXg7cZfG0%3DMtIPdyqSY4tQv0oDcf6KJx939IkYJYAuzhFUon3IJuMc4RmT7N"


def create_url():
    # Replace with user ID below
    user_id = 215939847 # start with bboczeng
    return "https://api.twitter.com/2/users/{}/followers".format(user_id)


def get_params():
    return {"user.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowersLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_followers():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    username_list = []
    for i in json_response['data']:
        username_list.append(i['username'])
    return username_list

def write_to_database(user_list):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="060920",
        database="twitter"
    )

    cursor = db.cursor()

    sql = """INSERT INTO account_info (
             id, username, name, description, location, profile_image_url, protected, verified, created_at,
             followers_count, following_count, listed_count, tweet_count
           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    for account in user_list:

        id = account["id"]
        username = account["username"]
        name = account["name"]
        description = account["description"]
        try:
            location = account["location"]
        except:
            location = None
        profile_image_url = account["profile_image_url"]
        protected = account["protected"]
        verified = account["verified"]
        created_at = account["created_at"]
        followers_count = account["public_metrics"]["followers_count"]
        following_count = account["public_metrics"]["following_count"]
        listed_count = account["public_metrics"]["listed_count"]
        tweet_count = account["public_metrics"]["tweet_count"]

        # insert the account info into the account_info table
        values = (id, username, name, description, location, profile_image_url, protected, verified, created_at,
                  followers_count, following_count, listed_count, tweet_count)
        cursor.execute(sql, values)

    # commit the changes to the database and close the connection
    db.commit()
    db.close()
        


if __name__ == "__main__":
    username_list = get_followers()
    user_list = get_userinfo.get_user_info(username_list)
    pprint.pprint(user_list[0])
    write_to_database(user_list)