import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None

def select_sum(conn, cat_code):
	cur = conn.cursor()
	cur.execute("SELECT SUM(amount) FROM tblRabobankMaster WHERE description = '%s';" % cat_code)
	rows = cur.fetchall()

	for row in rows:
		print(row)

