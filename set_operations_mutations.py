n = input('number of element: ')
s = set(map(int, raw_input('elements: ').split())) 
cmd = input('no of sets: ') 
for i in range(1,cmd+1):
  i = raw_input('set operation and total elements: ').split(' ')
  s2 = set(map(int, raw_input('elements: ').split()))
  k = 's'+'.'+i[0]+'(s2)'
  print k
  eval(k)
  print s
print 'final set',s
print sum(set(s))
