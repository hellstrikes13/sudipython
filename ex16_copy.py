from sys import argv
script , filename = argv
print "hey this is ur file %r" % filename
f = open(filename,'r')
txt = f.read()
print txt
