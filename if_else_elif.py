n = input("enter a number: ")
if n % 2 != 0:
    print "wierd"
elif n % 2 == 0 and n in range(2,6):
    print "Not wierd"
elif  n % 2 == 0 and n in range(6,21):
    print "Wierd"
elif n % 2 == 0 and n > 20:
    print "Not wierd"
else:
    print 'gl'
