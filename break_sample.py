n = [1,2,3,4,5,6,7]
count = 0
for i in range(len(n)):
  if i == 5:
   print 'break point',i
   break
  else:
   print 'adding:',n[i] , 'at position :',i,'th'
   count = count + n[i]
   print count
print '--' * 10
print 'final count:' , count

