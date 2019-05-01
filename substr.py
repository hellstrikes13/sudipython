#s = 'abcdcdc'
s = '12jlka445kljakldfjlaksjdfdka3942'
#s = 'TestCaseTestCase'
#s = 'I am an Indian, by birth.'
print 'string: ',s
print 'len str: ',len(s)
#s = 'ThIsisCoNfUsInG'
#sb = '23'
#sb = 'Birth'
sb = '3942'
#sb = 'CaseT'
#sb = 'cdc'
print 'substring: ',sb
print 'len substr: ',len(sb)
#sb = 'is'
count = 0
k = 0
sbl  = len(sb)
lst = []
while k < sbl:
   lst.append('s[i+'+str(k) +']')
   k = k + 1
str_to_be_comp = '+'.join(lst)
print str_to_be_comp
for i in range(len(s)-7):
 print eval(str_to_be_comp)
 if eval(str_to_be_comp) == sb:
  count = count + 1

print 'total count: ',count


