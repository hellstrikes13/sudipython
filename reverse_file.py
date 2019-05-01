f = open('test1','r')
i = 0
while True:
 s = f.readline()
 if len(s) == 0:
  break
 print s
 i = i + 1
f.close()
print 'total Number of lines: \t',i
