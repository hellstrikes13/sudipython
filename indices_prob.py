from __future__ import division
from itertools import combinations
n = input('no: ')
lst = []
#for i in range(n):
t = raw_input('elements: ')
lst.append(t)
# lst.append(i)
print 'printing list: ',lst
no_of_indices = input('indices no: ')
k =  list(combinations(lst,no_of_indices))
print k
lk = len(k)
cnt = 0
for q in k:
 if q[0] == "a":
  cnt = cnt + 1
prob = cnt / lk
print 'probabilty is: %.3f '%prob

