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
	for i in range(14):
		print(get_rows(f"/home/janan/TwitterChina/idiotbots_dot_com/data/profiles2/split_list{i}.db"))

