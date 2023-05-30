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
    for i in range(1, 16):
        try:
            merge_database("bigname/data/profiles/profile2.db", "bigname/data/new_profile0/profile"+ str(i) + ".db")
            print("Merged profile" + str(i) + ".db successfully!")
        except Exception as e:
            print("Error: " + str(e))
        
        # error: database 1, 3, 12
        