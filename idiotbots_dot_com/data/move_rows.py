import sqlite3

def move_rows(from_database, to_database, rows):
    conn = sqlite3.connect(from_database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT user FROM following_names LIMIT {rows}")
    selected_rows = cursor.fetchall()
    cursor.execute(f"DELETE FROM following_names WHERE rowid IN (SELECT rowid FROM following_names LIMIT {rows})")
    conn.commit()
    conn.close()
    conn = sqlite3.connect(to_database)
    cursor = conn.cursor()
    for row in selected_rows:
        cursor.execute("INSERT INTO following_names (user) VALUES (?)", (row[0],))
    conn.commit()
    conn.close()

def copy_all_rows(from_database, to_database):
    conn = sqlite3.connect(from_database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users")
    selected_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    conn = sqlite3.connect(to_database)
    cursor = conn.cursor()
    for row in selected_rows:
        # insert the whole row into the table
        try:
            cursor.execute("insert into users values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
        except Exception as e:
            print(f"Error: {e}")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # for i in range(14):
    #     move_rows(f'idiotbots_dot_com/data/profiles2/split_list{i}.db', f'idiotbots_dot_com/data/profiles2/split_list{i}.db', 50)
    #     print(f"Moved 50 rows from split_list{i}.db to the end of the table.")
    
    for i in [1, 3, 12]:
        copy_all_rows(f'idiotbots_dot_com/data/new_profile0/profile{i}.db', 'idiotbots_dot_com/data/profiles/profile_test.db')
        print(f"Moved 50 rows from profile{i}.db to the end of the table.")
