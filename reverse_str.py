import sys
a = str(raw_input('enter the string:\n'))
l = len(a)
i = 1
print 'Reversed string:'
while True:
 a1 = a[l-i]
 #print ''.join(a1)
# print ''.join(a1 for x in a1)
 sys.stdout.write(a1)
 i = i + 1
 if i == l+1:
  break
