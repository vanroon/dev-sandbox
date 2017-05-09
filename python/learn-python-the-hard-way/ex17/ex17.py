from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

#iin_file = open(from_file)
indata = (open(from_file)).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exixts? %r" % exists(to_file)
print "Ready, hit return to conitnue ctrlc to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()

