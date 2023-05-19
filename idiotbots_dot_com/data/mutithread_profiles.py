import twint
import multiprocessing
import sqlite3

def crawl(thread_id):
    c = twint.Config()
    c.User_full = True
    c.Database = f"/home/janan/TwitterChina/idiotbots_dot_com/data/profiles/profile{thread_id}.db"
    # database to list
    list = []
    conn = sqlite3.connect(f"/home/janan/TwitterChina/idiotbots_dot_com/data/profiles/split_list{thread_id}.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM following_names;")
    rows = cursor.fetchall()
    for row in rows:
        list.append(row[0])
    conn.close()
    print(len(list))
    for username in list:
        try:
            with multiprocessing.Pool(processes=1) as pool:
                c.Username = username
                # result = pool.apply_async(twint.run.Lookup(c))
                result = pool.apply_async(twint.run.Lookup, (c,))
                result.get(timeout=10)  # Set the timeout value here
            print(f"Thread {thread_id}: Profile lookup for {username} completed.")
            # remove the user in split_list database
            conn = sqlite3.connect(f"/home/janan/TwitterChina/idiotbots_dot_com/data/profiles/split_list{thread_id}.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM following_names WHERE user = '{username}';")
            conn.commit()
            cursor.close()  
            conn.close()
        except multiprocessing.TimeoutError:
            print(f"Thread {thread_id}: Timeout error.")
        except Exception as e:
            print(f"Thread {thread_id}: Error for {username}: {e}")

if __name__ == "__main__":

    processes = []
    thread_num = 7
    for thread in range(thread_num):
        p = multiprocessing.Process(target=crawl, args=(str(thread),))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()



# 99984
# 99987
# 99983
# 99985
# 99989
# 99987
# 95722


