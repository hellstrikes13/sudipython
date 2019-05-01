count  = 0
for i in range(4):
  count += 1
#  print count
  for x in range(0,count - 1):
   print '*',
  print '' 

print '-' * 20

print 'pattern A'
for i in range(1,6): print i * '*' + (5-i) * ''
'''
*
**
***
****
*****
'''

print '-' * 20

print 'pattern B'
for i in range(5,0,-1): print i * '*' + (5-i) * ''
'''
*****
****
***
**
*
'''

print '-' * 20

print 'pattern C'
for i in range(1,6): print (5-i) * ' ' + i * '*' 
'''
    *
   **
  ***
 ****
*****
'''

print '-' * 20

print 'pattern D'
for i in range(5,0,-1): print (5-i) * ' ' + i * '*' 
'''
*****
 ****
  ***
   **
    *
'''
print '-' * 20
print 'pattern E'
n=7
for i in range(n,1,-1): print i * '*' + ((n)-i)*' ' + ((n)-i)*' ' + i * '*' 
for i in range(1,n+1): print i * '*' + ((n)-i)*' ' + ((n)-i)*' ' + i * '*' 
