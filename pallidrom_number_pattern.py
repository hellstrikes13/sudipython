#n = input('number bol chal: ')
n = 5
for i in range(1,n+1):
  print ''.join(map(str,range(1,i+1)))+''.join(map(str,range(1,i)))[::-1]
