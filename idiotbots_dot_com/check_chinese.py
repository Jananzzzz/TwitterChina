import sqlite3
import json
import numpy as np
import matplotlib.pyplot as plt

def fetch_all_users(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# check name and bio and location whether it contains chinese
def check_chinese(text):
    for ch in text:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# check location
def check_location(location):
    china_locations = ['jiangsu', 'guangdong', 'macau', 'henan', 'hunan', 'shanghai', 'ningxia', 'taiwan', 'hubei', 'hongkong', 'xinjiang', 'sichuan', 'China', 'gansu', 'guangxi', 'fujian', 'beijing', 'zhejiang', 'guizhou', 'yunnan', 'qinghai', 'shanxi', 'shandong', 'aomen', 'anhui', 'jilin', 'hainan', 'neimenggu', 'chongqing', 'tianjin', 'hebei', 'heilongjiang', 'xizang', 'xianggang', 'liaoning', 'jiangxi', 'tibet']
    location0 = location.split(",")
    location1 = location.split(" ")
    for i in location0:
        if i.lower() in china_locations:
            return True
    for j in location1:
        if j.lower() in china_locations:
            return True
    if location is None:
        return True
    if location.lower() in china_locations:
        return True
    return False

# whether it followed the most popular chinese accounts
def whether_follow_ch(username):
    with open("idiotbots_dot_com/data/overall_list.json") as f:
        data = json.load(f)
        for i in data:
            if username in data[i]:
                return True

# check tweets

# check existence of a user
def check_existence(username):
    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile2.db")
    usernamelist = []
    for row in users:
        usernamelist.append(row[3])
    if username.lower() in usernamelist:
        print(f"{username} exists!")
    else:
        print(f"{username} does not exist!")

def count_chinese():
    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile2.db")
    usernamelist = []
    print(f"total users:{len(users)}")
    count_chinese = 0
    for row in users:
        user = {
            "name": row[2],
            "username": row[3],
            "bio": row[4],
            "location": row[5],
            "tweet": row[9],
            "following": row[10],
            "followers": row[11],
        } 
        if check_chinese(user["name"]) or check_chinese(user["bio"]) or check_chinese(user["location"]) or check_location(user["location"]):
            count_chinese += 1
    print(f"chinese users:{count_chinese}")

def distribution():
    follower_list = []
    following_list = []
    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile2.db")
    for row in users:
        follower_list.append(row[11])
        following_list.append(row[10])
    follower_list = np.array(follower_list)
    following_list = np.array(following_list)
    # bins: 0-1000, 1000-2000, 2000-3000, 3000-5000, 5000-10000, 10000-20000, 20000-50000, 50000-100000, 100000-200000, 200000-500000, 500000-inf
    bins = [0, 1000, 2000, 3000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, float("inf")]
    follower_hist = np.histogram(follower_list, bins=bins)
    following_hist = np.histogram(following_list, bins=bins)
    print(follower_hist)
    print(following_hist)
    plt.hist(follower_list, bins=bins)
    plt.show()
    plt.hist(following_list, bins=bins)
    plt.show()

def followers_rank():
    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile2.db")
    # rank users by followers
    userlist = []
    for row in users:
        user = {
            "name": row[2],
            "username": row[3],
            "bio": row[4],
            "location": row[5],
            "tweet": row[9],
            "following": row[10],
            "followers": row[11],
        } 
        userlist.append(user)
    userlist.sort(key=lambda x: x["followers"], reverse=False)
    for i in range(100):
        print(userlist[i]["username"], userlist[i]["followers"]) 


if __name__=="__main__":
    not_exist = [
        'yihong0618',
        'miableem',
        'nmslesebot',
        'realbingbingfan',
    ]
    check_existence("realbingbingfan")
    
