import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFFLlAEAAAAA71tnDgI6vXrQ9%2BGnMKuXg7cZfG0%3DMtIPdyqSY4tQv0oDcf6KJx939IkYJYAuzhFUon3IJuMc4RmT7N"


def create_url(username_list):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=fananshi"
    for i in username_list:
        usernames +=","+i
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_uid(username_list):
    url = create_url(username_list)
    json_response = connect_to_endpoint(url)
    for i in json_response['data']:
        print(i['id'])
    # print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    username_list = [
        "lidangzzz",
        "bboczeng",
    ]
    get_uid(username_list)