days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\n..."

print "Here are the days:", days,"a space"
print "Here are the months:", months

print '''
There is bla bla
single '
double "
escape \
'''

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
