s = raw_input('enter string1: ')
ana = raw_input('enter string2: ')
s1 =  ''.join(sorted(s))
s2 = ''.join(sorted(ana))
if s1 == s2:
    print 'Anagrams !!'
else:
    print 'Not Anagrams'
    
