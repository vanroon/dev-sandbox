import csv
#import MySQLdb

#files and databases
fname = '/home/pi/stack/SEGURA/BiznizRulez2.txt'
database = 'SEGURA'
tblBiznizRulez = 'tblBiznizRulez'
rulez_dict = {}

def connectMySql(host, user, db, passwd):
	import MySQLdb
	conn = MySQLdb.connect(host = host, user = user, db = db, passwd = passwd)
	return conn

def executeMySqlQuery(query):

	mydb = connectMySql('localhost', 'root', database, 'root')
	cursor = mydb.cursor()	

	try:
		cursor.execute(query)
		mydb.commit()
	except:
		mydb.rollback()

	mydb.close()

#truncate tblBiznizRulez
def truncateTable(table):
		
	mydb = connectMySql('localhost', 'root', database, 'root')
	cursor = mydb.cursor()

	qry = "TRUNCATE TABLE %s;" % table
	executeMySqlQuery(qry)


#read all lines and add to dict
def process_bizniz_rulez():
	
	#load all lines in list
	with open(fname) as f:
		content = f.readlines()
		
	for line in content:
		if line[0] != '#' and line.strip():
			line_list = line.rstrip().split('\t')
			rulez_dict[line_list[0]] = line_list[1]
	return rulez_dict
	
#for each entey create  query toninsert it
def createAndInsertQuery(dict):

	for key in dict:
		qry = "INSERT INTO tblBiznizRulez (categoryCode, categoryDescription) " \
				"VALUES ( "\
					"'%s', " \
					"'%s');"  % (key, dict[key])
		executeMySqlQuery(qry)


def main():

	dictionary = process_bizniz_rulez()
	truncateTable(tblBiznizRulez)
	createAndInsertQuery(dictionary)

main()


