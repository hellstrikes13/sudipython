from sys import argv
script , name = argv
prompt = ':-)'

print "hi %s , I'm the %s script ." %(name,script)
print "I'd like to ask u a few questions"
print "do u like me %s " % name
likes = raw_input(prompt)
print 'where do u live %s' %name
lives = raw_input(prompt)

print 'what kinda of computer u have ??'
pc = raw_input(prompt)
print """
 Alright u said %r about liking me.
u live in %r not sure where it is but sounds good
and u use %r computer .. which is nice
""" %(likes , lives , pc)
