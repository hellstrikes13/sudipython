'''
print a line of number chipak ke 
using just 1 line of code
'''
print ''.join(map(str,xrange(1,input('number: ')+1)))
print "".join(str(i) for i in xrange(1,input('number: ')+1))
