import psycopg2
import csv

def openPostgresConnection(dbname, user, host, password):
	try:
		connString = 'dbname=%s user=%s host=%s password=%s' % (dbname, user, host, password)
		conn = psycopg2.connect(connString)
	except:
		print "I am unable to connect"
	return conn

def closePostgresConnection(conn):
	conn.close()

def getColumnNames(tableName, dbname, user, host, password):
	conn = openPostgresConnection(dbname, user, host, password)
	qry = "SELECT column_name FROM information_schema.columns WHERE	table_name = '%s'" % tableName
	cur = conn.cursor()
	try:
		cur.execute(qry)
	except:
		print "I got an error!"

	rows = cur.fetchall()

	#trim the brackets and comma's
	columnsList = list()
	for i in rows:
		columnsList.append(str(i)[2:-3])

	closePostgresConnection(conn)
	return columnsList


def constructInsertQuery(tableName, dbname, user, host, password, fileName, line):
	columns = getColumnNames(tableName, dbname, user, host, password)
	# pop id column from list:
	columns.pop(0)
	#First part of query
	qry_1 = 	'''INSERT INTO %s ( ''' % tableName

	#column part of query
	qry_2 = ''' '''
	for column in columns:
		qry_2 += str(column)
		qry_2 += ', '
	#remove last comma and place parenthesis
	qry_2 = qry_2[:-2]+')'

	#Add query middle part
	qry_3 = ' VALUES ('

	#Add query data part
	qry_4 = ''

	lst = getValueList(line)

	for i in range(len(lst)):
		qry_4 += lst[i]
		qry_4 += ','
	#remove last comma and place parenthese
	qry_4 = qry_4[:-1]+')'

	qry = qry_1 + qry_2 + qry_3 + qry_4

	return qry

def processFile(fileName):
	csv_data = csv.reader(file(fileName), delimiter=',')
	for line in csv_data:
		insertIntoDatabase(line)

#Maybe skip this
def getValueList(fileName):
	valueList = list()
	csv_data = csv.reader(file(fileName), delimiter=',')
	for row in csv_data:

	someList = list()
	someList.append('aap')
	someList.append('noot')
	someList.append('mies')
	return csv_data




def main():
	tableName = 'tbl_master'
	dbname = 'SEGURA'
	user = 'gordon'
	host = 'localhost'
	password = 'password'
	dumpFile = 'C:\\Users\\Erik\\stack\\SEGURA\\Rabobank\\noDuplicatesMasterCsv.csv'
	cols = getColumnNames(tableName, dbname, user, host, password)
	qry = constructInsertQuery(tableName, dbname, user, host, password, dumpFile)
	#print cols
	print qry

main()




