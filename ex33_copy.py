numbers = []
def numbhai(num,incr):
 i = 0
 while i < num:
  print 'at the top i is %d' %i
  numbers.append(i)
  i = i + incr
  print 'numbers now:' ,numbers
  print 'at bottom i is %d ' % i
  print 'the numbers : '
numbhai(10,2)
print 'finally numbers are ' , numbers
