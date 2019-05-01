#!/bin/python

count = 1
n = raw_input('string: ')
for i in range(0,len(n)-1):
    if n[i] == n[i+1]:
        print 'consecutive chars',n[i]
        count +=1
    else:
        print 'non consecutive chars',n[i]
print 'final count: ',count
