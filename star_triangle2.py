n = input('no of lines in triangle: ')
if n % 2 == 0:
 print 'dude i need an odd number not an even number'
else:
 count = 0
 for i in range(n,0,-2):
  print count * ' ' + i * '*' + count * ' '
  count = count + 1
