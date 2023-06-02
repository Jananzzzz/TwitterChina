import sqlite3
import json
import os

dirctory_path = "/home/janan/TwitterChina/bigname/data/celebrity_data/"
username_list = []
for filename in os.listdir(dirctory_path):
    if filename.endswith(".db"):
        db_path = dirctory_path + filename
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT user From following_names"
        cursor.execute(query)
        users = cursor.fetchall()
        print(len(users))
        username_list.extend([user[0] for user in users])
        cursor.close()
        conn.close()

discrete_list = list(set(username_list))
print(f"following count: {len(discrete_list)}")

upers_list = []
with open("/home/janan/TwitterChina/bigname/data/overall_list.json") as f:
    data = json.load(f)
    for i in data:
        upers_list.append(data[i][20:])
for i in upers_list:
    if i not in discrete_list:
        discrete_list.append(i)
print(f"overall count: {len(discrete_list)}") # 700,000

# divide the list to eight parts
discrete_list0 = discrete_list[0:100000]
discrete_list1 = discrete_list[100000:200000]
discrete_list2 = discrete_list[200000:300000]
discrete_list3 = discrete_list[300000:400000]
discrete_list4 = discrete_list[400000:500000]
discrete_list5 = discrete_list[500000:600000]
discrete_list6 = discrete_list[600000:]

# write each list to a sqlite3 database
for i in range(7):
    batch_size = 1000
    conn = sqlite3.connect(f"/home/janan/TwitterChina/bigname/data/profiles/split_list{i}.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS following_names (user TEXT)")
    for j in range(0, len(eval(f"discrete_list{i}")), batch_size):
        list = eval(f"discrete_list{i}")
        batch = list[j:j + batch_size]
        values = [(user,) for user in batch]
        cursor.executemany("INSERT INTO following_names VALUES (?)", values)
        conn.commit()
    cursor.close()
    conn.close()
    print(f"Database {i} finished.")


# write each list to a txt file
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list0.txt", "w") as f:
#     for i in discrete_list0:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list1.txt", "w") as f:
#     for i in discrete_list1:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list2.txt", "w") as f:
#     for i in discrete_list2:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list3.txt", "w") as f:
#     for i in discrete_list3:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list4.txt", "w") as f:
#     for i in discrete_list4:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list5.txt", "w") as f:
#     for i in discrete_list5:
#         f.write(i + "\n")
# with open("/home/janan/TwitterChina/bigname/data/profiles/split_list6.txt", "w") as f:
#     for i in discrete_list6:
#         f.write(i + "\n")
