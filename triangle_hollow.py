line = 5
print (line-1) * " " + "*"
for i in xrange(1,line-1):
    print (line-i-1)* " " +  "*" + (2*i -1)*" " + "*"
print (line) * "* "
