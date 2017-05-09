from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit ctrl-c (^C)."
print "If you do want to erase, hit return."

raw_input("?")

print "Opening the file"
target = open(filename, 'w')
target.truncate()

print "Now i am going to ask you for three lines:"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i am writing this to a  file"

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally, we close it. "
target.close()


