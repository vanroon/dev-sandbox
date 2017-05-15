import sqlite3 as lite

def create_tables(sql, db):
	f = open(sql, 'r')                                                                                                             
	with f:
		data = f.read()
	con = lite.connect(db)
	with con:
		cur = con.cursor()
	cur.executescript(data)
