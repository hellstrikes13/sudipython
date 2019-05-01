print "\n\n"
#line = input('enter no of lines: ')
line = 5
for i in range((line-2),0,-1):
    print " " * (line-i-1)+ "* " + " " * (i-1)  + "*" + " " * (i-1) + " *" 

print " " * ((line+1)/2) + " * *" 
print "* " *  (line+1)
print " " * ((line+1)/2) + " * *" 

for i in xrange(1,line-1):
    print " " * (line-i-1)+ "* " + " " * (i-1)  + "*" + " " * (i-1) + " *" 
print "\n\n"
