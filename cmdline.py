import sys
print 'hello' ,sys.argv[1]
s = sys.argv[1]
print 'the string s:',s
s1 = '-'.join(s)
print 'join string with -:',s1
sp = s.split('/')
print 'split string:',sp
