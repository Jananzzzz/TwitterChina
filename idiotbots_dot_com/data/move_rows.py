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

if __name__ == '__main__':
    # for i in range(14):
    #     move_rows(f'idiotbots_dot_com/data/profiles2/split_list{i}.db', f'idiotbots_dot_com/data/profiles2/split_list{i}.db', 50)
    #     print(f"Moved 50 rows from split_list{i}.db to the end of the table.")
    
    for i in range(14):
            move_rows(f'idiotbots_dot_com/data/profiles2/split_list1.db', f'idiotbots_dot_com/data/profiles2/split_list{i}.db', 600)
            print(f"Moved 50 rows from split_list{i}.db to the end of the table.")
