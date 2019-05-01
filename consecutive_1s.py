#!/bin/python

s = 0
count = 0
rem = 0
n = int(raw_input('number: ').strip())
while(n>0):
    rem = n % 2
    n = n / 2
    if rem == 1:
        s +=1
        if s >= count:
            count=s
    else:
        s = 0
print 'Nos of 1s: ',count
        
