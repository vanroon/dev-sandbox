#!/usr/bin/python

#this script will set up the dev-segura database

# 1. remove segura.db if exists, else create
# 2. Run sql script that:
#	- creates tblRabobankMaster
#	- populates tblRabobankMaster

import sqlite3 as lite
import sys
import random

segura_db = 'segura.db'

def insert_transactions(num):
	from generate_iban import generate_iban
	from generate_iban import get_category_code_and_debcred



	con = lite.connect(segura_db)
	with con:
		cur = con.cursor()
		for x in range(1, num):
			selfAccount_val = 'NL44RABO0123456789'
			amount = 20 #random.randrange(1, 100, 5)
			crossAccount_val = generate_iban()
			category_code, debcred = get_category_code_and_debcred()

#			description_val = get_category_code()
#
#			if int(description_val[0]) > 2:
#				debcred = 'D'
#			else:
#				debcred = 'C'
			sql = "INSERT INTO \
				tblRabobankMaster ( \
					selfAccount, \
					amount, \
					crossAccount, \
					debcred, \
					description \
				) VALUES (	\
				 	'%s', \
					%s, \
					'%s', \
					'%s', \
					'%s' \
				)" % (selfAccount_val, amount, crossAccount_val, debcred, category_code)
					
			cur.execute(sql)

def create_tables(sqlfile, dbfile):		

	f = open (sqlfile, 'r')

	with f:
		data = f.read()

	con = lite.connect(dbfile)

	with con:
		cur = con.cursor()
		cur.executescript(data)
create_tables('segura.sql', 'segura.db')
insert_transactions(150)
