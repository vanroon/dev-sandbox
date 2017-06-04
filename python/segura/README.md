# Python SEGURA - Frist attempt

*segura2.sql* provisions an **existing** database (for sqlite3, 'SEGURA') with the following:
* tblMaster (Table with ALL data)
* vwSaving (View with transactions concerning saving account)

*segura_for_mysql.sql* provisions an **existing** database (for mysql, 'SEGURA') with the following:
* tblMaster (Table with ALL data)
* vwSaving (View with transactions concerning saving account)

*read_csv.py* loads the csv (pipe separated) MSSQL database dump from Master table in an **existing** mysql database. Based on a local out-of-the-box mysql server
p

*bank_codes.txt* provides some IBAN bank codes used by *setup.py* for creating test data
*category_codes.txt* provides cateogry-codes used for creating test data
*coutry_codes.txt* see description above

Have the following:
* python 2.x
* python-dev
* MySQLdb module
