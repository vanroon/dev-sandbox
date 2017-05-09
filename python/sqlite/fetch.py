#!/user/bin/python

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
	
	cur = con.cursor()
	cur.execute("SELECT * FROM Cars")

	rows = cur.fetchall()

	for row in rows:
		print row
