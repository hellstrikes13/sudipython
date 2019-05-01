vowels = 'aeiou'
nv = ''
vv = ''
s = 'sneha'
count = 0
count2 = 0
for i in s:
 if i not in  vowels: 
  nv = nv + i
  count = count + 1 
 else:
  vv = vv + i
  count2 = count2 + 1 
print 'non vowels :' , ' '.join(nv)
print 'count of non vowels is' , count
print 'vowels :', ' '.join(vv)
print 'count of vowels are',count2
