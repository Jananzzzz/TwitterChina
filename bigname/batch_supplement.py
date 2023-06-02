import json
import itertools
import time
import subprocess


username_list = []
# fetch failed list
with open("/home/janan/TwitterChina/bigname/data/celebrity_data/failed_list.json", "r") as f:
    failed_list = json.load(f)  
    for user in failed_list:
        username_list.append(failed_list[user])

# recrawl failed list

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

