from sys import argv

script, filename = argv

txt = open(filename)

print "Here is file %r:" % filename
a = txt.read()
print a

print "type filename:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


