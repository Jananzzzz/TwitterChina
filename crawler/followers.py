import requests
import os
import json
import get_uid

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


if __name__ == "__main__":
    username_list = get_followers()
    userid_list = get_uid.get_uid(username_list)
    for i in range(100):
        print(userid_list[i], username_list[i])