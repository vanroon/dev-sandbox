#!/usr/bin/python

#this script will set up the dev-segura database

# 1. remove segura.db if exists, else create
# 2. Run sql script that:
#	- creates tblRabobankMaster
#	- populates tblRabobankMaster

import sqlite3 as lite
import sys
import random

segura_db = 'segura2.db'

def insert_transactions(num):
	from generate_iban import generate_iban
	from generate_iban import get_category_code_and_debcred
	from generate_iban import get_category_code



	con = lite.connect(segura_db)
	with con:
		cur = con.cursor()
		for x in range(1, num):
			selfAccount_val = 'NL44RABO0123456789'
			currency = 'EUR'
			processDate = '01-01-2017'
			amount = random.randrange(1, 100, 5)
			crossAccount_val = generate_iban()
			category_code = get_category_code()
			description2 = "some piece of text and fir"
			description3 = "st part of word "
#			debcred = category_code[0]
			if category_code[:1] == '1':
				debcred = 'C'
			else:
				debcred = 'D'
#			description_val = get_category_code()
#
#			if int(description_val[0]) > 2:
#				debcred = 'D'
#			else:
#				debcred = 'C'
			sql = "INSERT INTO \
				tblMaster ( \
					selfAccount, \
					currency, \
					processDate, \
					debcred, \
					amount, \
					crossAccount, \
					description1, \
					description2, \
					description3 \
				) VALUES (	\
				 	'%s', \
					'%s', \
					'%s', \
					'%s', \
					%d, \
					'%s', \
					'%s', \
					'%s', \
					'%s' \
				)" % (selfAccount_val, currency, processDate, debcred, amount, crossAccount_val, category_code, description2, description3)
					
			cur.execute(sql)

def create_tables(sqlfile, dbfile):		

	f = open (sqlfile, 'r')

	with f:
		data = f.read()

	con = lite.connect(dbfile)

	with con:
		cur = con.cursor()
		cur.executescript(data)

class piggy(object):
	def __init__(self, name):
		self.name = name

	
	def getName():
		return name



create_tables('segura2.sql', 'segura2.db')
insert_transactions(150)
a = piggy('104-1 moto')
print a.getName()
