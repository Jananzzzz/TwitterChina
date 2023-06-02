# don't use mv, use cp, then rm
import sqlite3
import json
import time  
# always use time module to have an understanding of how long your code takes
import twint
import os
import signal


dirctory_path = "/home/janan/TwitterChina/bigname/data/celebrity_data/"
username_list = []
count = 0
for filename in os.listdir(dirctory_path):
    if filename.endswith(".db"):
        db_path = dirctory_path + filename
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT user From following_names"
        cursor.execute(query)
        users = cursor.fetchall()
        print(len(users))
        count += 1
        username_list.extend([user[0] for user in users])
        cursor.close()
        conn.close()

print(f"overall following: {len(username_list)}")
print(f"average following: {len(username_list)/count}")
discrete_list = list(set(username_list))
print(f"discret following: {len(discrete_list)}")

upers_list = []
with open("/home/janan/TwitterChina/bigname/data/overall_list.json") as f:
    data = json.load(f)
    for i in data:
        upers_list.append(data[i][20:])
for i in upers_list:
    if i not in discrete_list:
        discrete_list.append(i)
print(f"overall count: {len(discrete_list)}")

def fetch_all_users(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM following_names;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def fetch_all_users0(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# account not exist
account_not_exist = []
for i in range(14):
    users = fetch_all_users(f"bigname/data/profiles2/split_list{i}.db")
    for row in users:
        account_not_exist.append(row[0])
print(f"account not exist: {len(account_not_exist)}")

# account already crawled
account_already_crawled = []
for i in range(2, 14):
    users = fetch_all_users0(f"bigname/data/profiles/profile{i}.db")
    for row in users:
        account_already_crawled.append(row[3])
print(f"account already crawled: {len(account_already_crawled)}")


# new_list = discrete_list - account_not_exist - account_already_crawled
new_list = list(set(discrete_list) - set(account_not_exist) - set(account_already_crawled))
print(f"new_list: {len(new_list)}")

# split the new_list into 16 parts, store them in 16 sqlite3 databases (table name: users, column name: user (TEXT))
for i in range(16):
    conn = sqlite3.connect(f"bigname/data/new_split/split_list{i}.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS following_names (user TEXT);")
    conn.commit()
    if i != 15:
        list = new_list[i*len(new_list)//16:(i+1)*len(new_list)//16]
        print(f"list{i}: {len(list)}")
    else:
        list = new_list[i*len(new_list)//16:]
        print(f"list{i}: {len(list)}")
    for user in list:
        cursor.execute(f"INSERT INTO following_names VALUES ('{user}');")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"split_list{i}.db created.")