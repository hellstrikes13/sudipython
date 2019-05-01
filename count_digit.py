def digcount(n):
 c = 0
 while n != 0:
  print 'n: %d'%n
  print 'increment count by 1 ' 
  c = c + 1
  print 'count: %d'%c
  print 'dividing n by 10'
  n = n / 10
#  print 'now n:%d'%n
 else:
  print 'sinc n == 0 hence exiting the loop'
 print '------------------------------'
 print 'total number of digits are %r'%c 

digcount(123)
