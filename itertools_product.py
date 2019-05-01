from itertools import product
a = [5,6]
b = [3,4]
ab = (a,b)
print list(product(*ab))
combi = sorted(list(product(*ab)))
print combi

print ' '.join(str(i) for i in combi)

