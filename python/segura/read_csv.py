import csv
import MySQLdb

# files and databases
dump_file = '/home/pi/stack/SEGURA/Rabobank/MSSQL_Dump/total_dump_20170602.csv'
database = 'SEGURA'

#Use this file to import a csv dump (pipe-separated) from MSSQL Segura DB

mydb = MySQLdb.connect(host='localhost', user='root', db=database, passwd='root')
cursor = mydb.cursor()

#Load all data from csv file in a variable
csv_data = csv.reader(file(dump_file), delimiter='|')
for row in csv_data:

#The if statement below was to cut a decimal to only 2 digits after the point. 
#I found this messed up the totals so it's not used.
	#	if ',' in row[4]:
	#		row[4] = row[4][0:row[4].find(',')+3] 

#substitue ',' with '.'
	row[4] = row[4].replace(',','.')

	sql = 'INSERT INTO tblMaster(' \
								'selfAccount, '\
								'currency, '\
								'processDate, '\
								'debcred, '\
								'amount, '\
								'crossAccount, '\
								'crossAccountHolder, '\
								'interestDate, '\
								'typ, '\
								'unknown1, '\
								'description1, '\
								'description2, '\
								'description3, '\
								'description4, '\
								'unknown2, '\
								'unknown3, '\
								'transactionReference,' \
								'incassantId, ' \
								'kenmerkMachtiging' \
							') VALUES (' \
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'%s, '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s", '\
								'"%s" '\
								');' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18])
	try:
	
		cursor.execute(sql)
		print "success"
	except:
		print "got error!"
	print sql
mydb.commit()
cursor.close()
