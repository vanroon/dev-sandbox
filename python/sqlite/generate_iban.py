#!/usr/bin/python

def generate_iban():
	
	import random

	def get_country_code():
		country_codes_file = 'country_codes.txt'
		# get country codes from file 'country_codes.txt'

		def random_line(afile):
			with open(afile) as f:
				line = next(f)
				for num, aline in enumerate(f):
					if random.randrange(num + 2): continue
					line = aline
				return line.rstrip()	
		return random_line('country_codes.txt')

	def generate_country_number():
		country_number = ""
		for x in range(2):
			country_number += str(random.randint(0,9))
		return country_number
	
	def get_bank_code():
		bank_codes_file = 'bank_codes.txt'
		# get codes from bank_codes.txt'

		def random_line(afile):
			with open(afile) as f:
				line = next(f)
				for num, aline in enumerate(f):
					if random.randrange(num + 2): continue
					line = aline
				return line.rstrip()
		return random_line(bank_codes_file)

	def generate_account_number():
		account_number = \
			"0" + str(random.randint(100000000, 999999999))
		return account_number

	
	iban = ""
	iban += get_country_code()
	iban += generate_country_number()	
	iban += get_bank_code()
	iban += generate_account_number()
	return iban

print generate_iban()
