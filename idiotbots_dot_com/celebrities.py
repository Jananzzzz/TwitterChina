import os
import json
import subprocess
import time

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

username_list = []
for link in overall_list:
    username_list.append(link[20:])





command = "twint -u bboczeng --database bboczeng.db --following > /dev/null 2>&1"
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# get the pid of the process
pid  = proc.pid

# check if the process is still running
while proc.poll() is None:
    print("Process is still running...")
    time.sleep(3)

if proc.returncode == 0:
    print("Process finished successfully.")
else:
    print("Process finished with error or warning.")



# with open(f"/home/janan/TwitterChina/idiotbots_dot_com/data/overall_list.json", "w") as f:
#     dict = {}
#     for idx, link in enumerate(overall_list):
#         dict[f"{idx}"] = link
#     json_data = json.dumps(dict, indent=4)
#     f.write(json_data)

# basic usage of twint:
# twint -u bboczeng --database bboczeng.db --followers > /dev/null 2>&1 &
# twint -u bboczeng --database bboczeng.db --following > /dev/null 2>&1 &
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
