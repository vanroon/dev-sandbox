from abc import ABCMeta, abstractmethod

#Class IterRegistry keeps track of all objects that are instantiated of a class
class IterRegistry(type):
	def __iter__(cls):
		return iter(cls._registry)


class Account(object):
	"""Base class for accounts.
	This class's metaclass is set to ABCMeta and one of its methods is virtuals. This
	makes it an Abstract Base Class.

	source: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
	
	Attributes:
		iban
	"""
	
	__metaclass__ = ABCMeta

	iban = ""

	def __init__(self, iban):
		"""Returns a new Account"""
		self.iban = iban

	@abstractmethod
	def account_type(self):
		pass

class SelfAccount(Account):
	__metaclass__ = IterRegistry
	_registry = []
	
	def account_type(self):
		return 'self'

class CrossAccount(Account):
	
	def account_type(self):
		return 'cross'


class Transaction(object):
	
	def __init__(self, SelfAccount, CrossAccount, amount):
		"""Returns a new transaction"""
		self.id = id 
		self.SelfAccount = SelfAccount.iban
		self.CrossAccount = CrossAccount.iban
		self.currency = currency
		self.processDate = processDate
		self.debcred = debcred
		self.amount = amount
		self.description = description

class Piggy(object):
	__metaclass__ = IterRegistry
	_registry = []
	"""A Piggy (bank) consists of a set of transaction that fall under one category_code"""

	def __init__(self, category_code, Transaction):
		self.category_code = category_code
		self.amount = Transaction.amount

	# getBalance will returns the sum of a given set of transactions
	def getBalance(category_code):
		total = 0
		sql = "SELECT SUM(amount) FROM tblRabobankMaster WHERE description = '%s';" % category_code
		db_file = 'segura.db'
	
		import sqlite3
		from sqlite3 import Error
	
		try:
			conn = sqlite3.connect(db_file)
			return conn
		except Error as e:
			print(e)

		cur = conn.cursor()
		cur.execute(sql)

		rows = cur.fetchall()
		for row in rows:
			print (row)
			
		execute_sql(sql, database)





a = SelfAccount('NL44RABO1234567890')
b = CrossAccount('SE32HAAS1932193210')
print a.account_type()
print b.account_type()

