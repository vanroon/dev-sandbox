from abc import ABCMeta, abstractmethod

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
	
	def account_type(self):
		return 'self'

class CrossAccount(Account):
	
	def account_type(self):
		return 'cross'
