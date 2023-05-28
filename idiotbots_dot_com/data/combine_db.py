import sqlite3

def merge_database(database1, database2):
    conn = sqlite3.connect(database1)
    cursor = conn.cursor()
    cursor.execute("ATTACH DATABASE ? AS db2", (database2,))
    conn.commit()
    cursor.execute("INSERT INTO users SELECT * FROM db2.users")
    conn.commit()
    cursor.execute("DETACH DATABASE db2")
    conn.commit()
    conn.close()

if __name__=="__main__":
    for i in range(3, 14):
        merge_database("idiotbots_dot_com/data/profiles/profile2.db", "idiotbots_dot_com/data/profiles/profile"+ str(i) + ".db")
        print("Merged profile" + str(i) + ".db successfully!")