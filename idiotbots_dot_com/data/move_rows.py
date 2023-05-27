import sqlite3

def move_rows(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT user FROM following_names LIMIT 50")
    selected_rows = cursor.fetchall()
    cursor.execute("DELETE FROM following_names WHERE rowid IN (SELECT rowid FROM following_names LIMIT 50)")
    for row in selected_rows:
        cursor.execute("INSERT INTO following_names (user) VALUES (?)", (row[0],))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    for i in range(14):
        move_rows(f'idiotbots_dot_com/data/profiles2/split_list{i}.db')
        print(f"Moved 50 rows from split_list{i}.db to the end of the table.")
