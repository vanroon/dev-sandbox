def getCursor():
	import MySQLdb
	
	conn = MySQLdb.connect( host = 'localhost', \
				user = 'root', \
				db = 'SEGURA',
				passwd = 'root') 
	return conn 


def insertIntoSegura(query):

	import MySQLdb
	import sys
	
	
	conn = getCursor()
	
	cursor = conn.cursor()
	try:
		cursor.execute(query)
	except:
		print "got error"
	
	conn.commit()
	conn.close()


def selectFromSegura(query):
	import MySQLdb
	conn = getCursor()
	cursor = conn.cursor()	

	try:
		cursor.execute(query)
		results = cursor.fetchall()
		return results
		cursor.close()
	except:
		print "Error! Can not execute select query"
	
		cursor.close()	
