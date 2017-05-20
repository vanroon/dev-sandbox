#!/usr/bin/python
def setPiggies(filename):
	"""This method reads the piggyfile and creates piggy objects from that file. The file
	contains a category code and a name. The default filename is piggies.txt"""	
	import csv

	codes = []
	names = []
	with open(filename, 'r') as f:
		reader = csv.reader(f, delimiter = '\t')
		for code, name in reader:
			codes.append(code)
			names.append(name)
		
		i = 0	
		piggies = []	
		for code in codes:
			piggies.append(Piggy(code, names[i]))
			i += 1	
