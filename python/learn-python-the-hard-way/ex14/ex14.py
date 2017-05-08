from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I am script %s." % (user_name, script)
print "do you, %s ?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What computer do you have?"
computer = raw_input(prompt)

print """
Aight,
Likes: %r
Lives: %r
Comp: %r
""" % (likes, lives, computer)
