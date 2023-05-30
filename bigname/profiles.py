# twint --user-full --userlist inputlist.txt --database profiles.db

import sqlite3
import json
import time  
# always use time module to have an understanding of how long your code takes
import twint
import os
import signal


dirctory_path = "/home/janan/TwitterChina/idiotbots_dot_com/data/celebrity_data/"
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
with open("/home/janan/TwitterChina/idiotbots_dot_com/data/overall_list.json") as f:
    data = json.load(f)
    for i in data:
        upers_list.append(data[i][20:])
for i in upers_list:
    if i not in discrete_list:
        discrete_list.append(i)
print(f"overall count: {len(discrete_list)}")

assert False

checklist= [
    "MiaBleem",
    "bboczeng",
    "haoel",
    "fndroid"
]

for i in checklist:
    if i in discrete_list:
        print(f"{i} in discrete_list")

def timeout_handler(signum, frame):
    raise Exception("Timeout!")

start_time = time.time()
c = twint.Config()
c.User_full = True
c.Database = "/home/janan/TwitterChina/idiotbots_dot_com/data/profiles.db"
for i in range(len(discrete_list)):
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)
        c.Username = discrete_list[i]
        twint.run.Lookup(c)
        signal.alarm(0)
    except TimeoutError:
        print("Timeout!")
    except Exception as e:
        print(e)
    if (i+1) % 100 == 0:
        tmp_time = time.time()
        print(f"crawled {i+1} users. Average time cost per user: {(tmp_time - start_time)/(i+1)}")
    # # check the username in database or not
    # query = "SELECT * FROM users WHERE username = ?"
    # value = (username,)
    # cursor.execute(query, value)
    # result = cursor.fetchone()
    # if result is None:
    #     try:
    #         c.Username = username
    #         c.User_full = True
    #         c.Database = "/home/janan/TwitterChina/idiotbots_dot_com/data/profiles.db"
    #         twint.run.Lookup(c)
    #     except Exception as e:
    #         print(e)
    # else:
    #     print(f"{username} already in database.")
    
end_time = time.time()
print(f"Crawl Twitter of China core took time: {end_time - start_time}")

