s = 'BANANA'
lst = []
for i in range(len(s)):
 if s[i] == 'A' or s[i] ==  'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
   print s[i:]
   print '---------'
   for k in s[i:]:
    print k
    #lst.append(k)
    #print ''.join(lst) 
 #else:
#        stu = stu + 1
