from collections import defaultdict,Counter
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
print d
for i in d.items():
    print i
