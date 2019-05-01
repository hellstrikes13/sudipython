r = 0
count = 0
for i in range(1,11):
    for q in range(1,11):
        if (q+count) % 7 == 0 and (q+count) % 11 == 0:
            print 'blah',
        else:
            print "%4d"%(q+count),
    print " "
    r = r + 1
    count = 0
    count = count + (10*r)
