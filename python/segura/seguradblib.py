def getCursor():
	import MySQLdb
	
	conn = MySQLdb.connect( host = 'localhost', \
				user = 'root', \
				db = 'SEGURA') 
	return conn.cursor() 


def insertIntoSegura(query):

	import MySQLdb
	
	
	cursor = getCursor()

	try:
		cursor.execute(query)
	except:
		print "got error", sys.exec_info()[0]
	
	mydb.commit()
	cursor.close()


def selectFromSegura(query):
	import MySQLdb
	cursor = getCursor()
	
	try:
		cursor.execute(query)
		results = cursor.fetchall()
		return results
		cursor.close()
	except:
		print "Error! Can not execute select query"
	
		cursor.close()	
