n = input('number of element: ')
s = set(map(int, raw_input('elements: ').split())) 
cmd = input('no of set operations: ') 
for i in range(1,cmd+1):
 i = raw_input('ops and ele: ').split(' ')
 if len(i) == 1:
  k = 's'+'.'+i[0]+'()'
  print k
  eval(k)
  print s
 else:
  k = 's'+'.'+i[0]+'('+i[1]+')'
  print k
  eval(k)
  print s
print 'final set',s
print sum(set(s))
