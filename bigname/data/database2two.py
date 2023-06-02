import sqlite3

def split_database(input_file, output_file1, output_file2):
    # Connect to the input database
    conn = sqlite3.connect(input_file)
    cursor = conn.cursor()

    # Count the number of rows in the table
    cursor.execute(f"SELECT COUNT(*) FROM following_names")
    num_rows = cursor.fetchone()[0]
    print(num_rows)

    # Split the table into two halves
    cursor.execute(f"SELECT * FROM following_names LIMIT {num_rows//2} OFFSET 0")
    rows1 = cursor.fetchall()
    cursor.execute(f"SELECT * FROM following_names LIMIT {num_rows - (num_rows//2)} OFFSET {num_rows//2}")
    rows2 = cursor.fetchall()

    # Create the first output database and write the first half of the rows
    conn1 = sqlite3.connect(output_file1)
    cursor1 = conn1.cursor()
    cursor1.execute(f"CREATE TABLE following_names (user TEXT NOT NULL)")
    cursor1.executemany(f"INSERT INTO following_names VALUES ({','.join('?'*len(rows1[0]))})", rows1)
    conn1.commit()

    # Create the second output database and write the second half of the rows
    conn2 = sqlite3.connect(output_file2)
    cursor2 = conn2.cursor()
    cursor2.execute(f"CREATE TABLE following_names (user TEXT NOT NULL)")
    cursor2.executemany(f"INSERT INTO following_names VALUES ({','.join('?'*len(rows2[0]))})", rows2)
    conn2.commit()

    # Close the connections
    cursor.close()
    cursor1.close()
    cursor2.close()
    conn.close()
    conn1.close()
    conn2.close()

if __name__ == "__main__":
    for i in range(7):
        split_database(f"/home/janan/TwitterChina/bigname/data/profiles/split_list{i}.db", 
                       f"/home/janan/TwitterChina/bigname/data/profiles2/split_list{i}.db", 
                       f"/home/janan/TwitterChina/bigname/data/profiles2/split_list{i+7}.db")
        print(f"Splitting profile{i}.db completed.")