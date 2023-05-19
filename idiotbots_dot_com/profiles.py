# twint --user-full --userlist inputlist.txt --database profiles.db

import json
import time  
# always use time module to have an understanding of how long your code takes
import twint

username_list = []

with open("/home/janan/TwitterChina/idiotbots_dot_com/data/overall_list.json") as f:
    data = json.load(f)
    for i in data:
        username_list.append(data[i][20:])

# write username list to a txt file
# with open("/home/janan/TwitterChina/idiotbots_dot_com/data/username_list.txt", "w") as f:
#     for i in username_list:
#         f.write(i + "\n")

c = twint.Config()
for username in username_list:
    try:
        c.Username = username
        c.User_full = True
        c.Database = "/home/janan/TwitterChina/idiotbots_dot_com/data/profiles.db"
        twint.run.Lookup(c)
    except Exception as e:
        print(e)
