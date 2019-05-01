count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for c in count:
 print 'count : %d' %c

for f in fruits:
 print 'fruit : %s' %f

for c in change:
 print 'change : %r' %c

elem = []
r = range(1,6)
elem.append(r)
for e in elem:
 print 'element was %r' %e
