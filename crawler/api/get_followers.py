import requests
import mysql.connector
import pprint
import os
import json
import get_userinfo
import config

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = config.bear_token


def create_url(userid):
    # Replace with user ID below
    user_id = userid # start with bboczeng
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


def get_followers(userid_list):
    username_list = []
    for i in userid_list:

        url = create_url(i)
        params = get_params()
        json_response = connect_to_endpoint(url, params)
        # print(json.dumps(json_response, indent=4, sort_keys=True))
        username_list = []
        for j in json_response['data']:
            username_list.append(j['username'])
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
        
        cursor.execute("SELECT id from account_info WHERE id = %s", (account["id"],))
        result = cursor.fetchone()

        if result is not None:
            continue
        else:
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

    # get the first 100 follower's info
    userid_list = [
        "1644979953484562432"
    ]
    username_list = get_followers(userid_list)
    user_list = get_userinfo.get_user_info(username_list)
    write_to_database(user_list)

    # get the first 100 follower's follower's info
    while True: 
        new_userid_list = []
        for i in user_list:
            new_userid_list.append(i["id"])
            username_list = get_followers(new_userid_list)
            user_list = get_userinfo.get_user_info(username_list)
            write_to_database(user_list)
        

