import os
import json

def form_list(list_name):
    list = []
    folder_path = f"/home/janan/TwitterChina/idiotbots_dot_com/data/{list_name}"
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path) as f:
            user_info = json.load(f)
            for user_name in user_info:
                if user_info[user_name] not in list:
                    list.append(user_info[user_name])
    
    for idx, info in enumerate(list):
        print(idx, info)

    # with open(f"/home/janan/TwitterChina/idiotbots_dot_com/data/{list_name}_list.json", "w") as f:
    #     dict = {}
    #     for idx, link in enumerate(list):
    #         dict[f"{idx}"] = link
    #     json_data = json.dumps(dict, indent=4)
    #     f.write(json_data)

    return list

popularity_list = form_list("popularity")
activity_list = form_list("activity")
overall_list = []
for i in popularity_list:
    if i not in overall_list:
        overall_list.append(i)
for j in activity_list:
    if j not in overall_list:
        overall_list.append(j)

# with open(f"/home/janan/TwitterChina/idiotbots_dot_com/data/overall_list.json", "w") as f:
#     dict = {}
#     for idx, link in enumerate(overall_list):
#         dict[f"{idx}"] = link
#     json_data = json.dumps(dict, indent=4)
#     f.write(json_data)

# basic usage of twint:
# twint -u bboczeng --database bboczeng.db --followers > /dev/null 2>&1 &
# twint -u bboczeng --database bboczeng.db --followers > /dev/null 2>&1 &
# twint --user-full --userlist inputlist.txt --database profiles.db

# bash script case:
"""
#!/bin/bash

userlist=("sss" "fsad" "sdfa" "sfda" "fdsl")

for user in "${userlist[@]}"; do
    twint -u "$user" --database "$user.db" --followers > /dev/null 2>&1 &
done
"""

# python code case:
"""
import subprocess

userlist = ["sss", "fsad", "sdfa", "sfda", "fdsl"]

for user in userlist:
    command = f'twint -u {user} --database {user}.db --followers > /dev/null 2>&1 &'
    subprocess.run(command, shell=True)
"""
