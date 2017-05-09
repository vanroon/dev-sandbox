def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_non():
	print "no printszz"

print_two("Erik", "van Roon")
print_two_again("Erik", "de tweede")
print_one("First")
print_non()
