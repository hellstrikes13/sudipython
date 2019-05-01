line = 5
print "* " * (line)
for i in range((line-2),0,-1):
 print " " * (line-i-1)+ "*" + " " *(2*i-1) + "*" 
print " " * ((line/2)+1)+ " *"
