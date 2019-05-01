numbers = []
def numbhai(num):
 i = 0
 for i in range(0,num):
  print 'at the top i is %d' %i
  numbers.append(i)
#  i = i + 1
  print 'numbers now:' ,numbers
  print 'at bottom i is %d ' % i
numbhai(5)
print 'finally numbers are ' , numbers
