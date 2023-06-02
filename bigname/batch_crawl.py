import time
import itertools
import os
import json
import subprocess

def form_list(list_name):
    list = []
    folder_path = f"/home/janan/TwitterChina/bigname/data/{list_name}"
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path) as f:
            user_info = json.load(f)
            for user_name in user_info:
                if user_info[user_name] not in list:
                    list.append(user_info[user_name])
    
    # with open(f"/home/janan/TwitterChina/bigname/data/{list_name}_list.json", "w") as f:
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

user_list = [
    "bboczeng",
    "lidangzzz",
    "UziQ4Q",
    "thecalicastle",
    "youyuxi",
    "himself_65",
    "fananshi",
    "MiaBleem",
    "haoel"
]


command_template = "twint -u {user} --database bigname/data/celebrity_data/{user}.db --following > /dev/null 2>&1"

# create a cycle that will cycle through the list of users indefinitely
user_cycle = itertools.cycle(username_list)

check_all_processes = 0
already_finished = []
failed = []

start_time = time.time()
# start the first four processes
processes = []
for i in range(8):
    user = next(user_cycle)
    command = command_template.format(user=user)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"{check_all_processes}  Started process for {user}")
    check_all_processes += 1
    already_finished.append(user)
    processes.append((user, proc))

# loop until all the processes have completed
try:
    while processes:
        for user, proc in processes:
            # check if the process has completed
            if proc.poll() is not None:
                if proc.returncode == 0:
                    #   print(f"---------------------------------------Process for {user} finished successfully.")
                    pass
                else:
                    print(f"---------------------------------------Process for {user} finished with error or warning.")
                    failed.append(user)

                # remove the process from the list of processes
                processes.remove((user, proc))
                # start a new process for the next user, if there is one
                next_user = next(user_cycle, None)
                if next_user is not None:
                    command = command_template.format(user=next_user)
                    new_proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"{check_all_processes}Started process for {next_user}")
                    check_all_processes += 1
                    already_finished.append(next_user)
                    processes.append((next_user, new_proc))
            if not processes:
                # All processes are done, break the loop
                break
        if check_all_processes == len(username_list):
            # All processes are done, break the loop
            break
        time.sleep(3)
except Exception as e:
    print(e)

with open(f"/home/janan/TwitterChina/bigname/data/celebrity_data/finished_list.json", "w") as f: 
    dict = {} 
    for idx, user in enumerate(already_finished): 
        dict[f"{idx}"] = user 
    json_data = json.dumps(dict, indent=4) 
    f.write(json_data)

with open(f"/home/janan/TwitterChina/bigname/data/celebrity_data/failed_list.json", "w") as f:
    dict = {}
    for idx, user in enumerate(failed):
        dict[f"{idx}"] = user
    json_data = json.dumps(dict, indent=4)
    f.write(json_data)


end_time = time.time()
print(f"Total time: {end_time - start_time} seconds")
