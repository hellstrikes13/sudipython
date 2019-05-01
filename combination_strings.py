from itertools import combinations
s = raw_input('string and repetation: ').split(' ')
st = sorted(s[0])
i = int(s[1])
for i in range(1,i+1):
 k = list(combinations(st,i))
 for r in k:
  print ''.join(r)
