# Naive Multiplication
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
	print 'we are x and y:',x,y
        z = z + y
	print 'i m z:',z
        x = x - 1
	print '\t\ti m x:',x
    return z

print naive(4,5)
