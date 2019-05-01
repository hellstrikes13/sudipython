n = input('no of lines in triange: ')
if n % 2 == 0:
 print 'sorry i dont like even number gimme an odd number'
else:
 count = n/2
 for i in range(1,n+1,2):
  print count * ' ' + i * '*' + count * ' '
  count = count - 1
 

'''
  *   
 ***
*****

'''
