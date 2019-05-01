n,m = 7,21

for i in xrange(1,n,2): 
    print ((i*".|.").center(m,'-'))

print 'WELCOME'.center(m,'-')

for i in xrange(n-2,-1,-2): 
    print ((i*".|.").center(m,'-'))
