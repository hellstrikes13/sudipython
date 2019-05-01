def fact(n):
 fac = 1
 while n != 0:
  fac = fac * n
#  print 'fact val:%r'%fac
  n = n - 1
#  print ' n was decremented by 1 so n is %r' %n
 return fac
ans = fact(6)
print 'factorial is %r ' %ans
