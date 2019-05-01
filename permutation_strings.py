from itertools import permutations
s = raw_input('string and repetation: ').split(' ')
st = s[0]
i = int(s[1])
strpermi  = sorted(list(permutations(st,i)))
for i in strpermi:
 print ''.join(i)

