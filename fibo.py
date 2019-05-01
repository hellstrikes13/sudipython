a,b = 0,1
fib = 0
n = input('enter the range u wanna generate fibonacci series: ')
print '\nfibo series:' 
print a,b,
for i in range(1,n-1):
  fib = a + b
  a = b
  b = fib
  print fib,
