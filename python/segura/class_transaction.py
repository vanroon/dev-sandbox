#!/usr/bin/python

def Transaction:
	'Common base class for all transactions'
	
	def __init__(	self, \
			currency, \
			processDate, \
			debcred, \
			amount, \
			description):
		self.currency = currency
		self.processDate = processDate
		self.debcred = debcred
		self.amount = amount
		self.description
