f = open('test1','r')
g = open('test2','w')
s = f.readlines()
r = s[::-1]
for i in r:
 g.write(i)

f.close()
g.close()
