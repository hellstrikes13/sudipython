line = 5
print "* " * (line+2)
for i in range((line-1),0,-1):
 print " " * (line - i -1) + " *" + " " * i + " " + " " * i + "*"  
print " " * (line -2)+"   *"
