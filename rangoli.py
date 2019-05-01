import string
n = 3
o = (map(chr,range(65,65+n)))
r = map(chr,range(65,65+n))[:0:-1]

print '-'.join(r) +'-' +'-'.join(o)

print "=" * 10
for i in (map(chr,range(34+1,34+n))):
 print  i + chr(ord(i) +1 )

'''
print 'this is 5th line from both sides'
for i in range(n,1,-1):
 print i
'''
a = '''
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''
