#!/usr/bin/python

import sqlite3 as lite
import sys

def readData():
	f = open ('segura.sql', 'r')
		
	with f:
		data = f.read()
		return data

con = lite.connect('test.db')

with con:

	cur = con.cursor()

	sql = readData()
	cur.executescript(sql)

	cur.execute("SELECT * FROM tblRabobankMaster")

	rows = cur.fetchall()

	for row in rows:
		print row
