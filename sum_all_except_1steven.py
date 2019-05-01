n = [1,2,3,5,3,6]
n1 = []
count = 0
for i in range(len(n)-1):
  if n[i] % 2 == 0:
   print n[i]
   print 'first even number', n[i] ,'ocurs at position:',i+1,'th'
   print 'original n:',n
   n1.append(n[i])
   n.pop(i)
   print 'n1:', n1
   print 'n',n
   total = sum(n)
   print 'total',total
   break
  else:
#   print 'in else block ',n[i]
   n1.append(n[i])
   print n1
   t = sum(n1)
print 'total2',t
'''
   print 'original n:',n
   n1.append(n[i])
   n.pop(i)
   print 'n1:', n1
   print 'n',n
   total = sum(n)
   print 'total',total
'''
