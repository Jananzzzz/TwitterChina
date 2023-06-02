import sqlite3

def get_rows(database):
	conn = sqlite3.connect(database)
	cursor = conn.cursor()
	cursor.execute("select count(*) from following_names")
	count = cursor.fetchone()[0]
	cursor.close()
	conn.close()
	return count

if __name__=="__main__":
	for i in range(16):
		print(get_rows(f"/home/janan/TwitterChina/bigname/data/split/split_list{i}.db"))

