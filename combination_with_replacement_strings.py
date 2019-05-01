from itertools import combinations_with_replacement
s = raw_input('string and repetation: ').split(' ')
st = sorted(s[0])
i = int(s[1])
k = list(combinations_with_replacement(st,i))
for r in k:
  print ''.join(r)
