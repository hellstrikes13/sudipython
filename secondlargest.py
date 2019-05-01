n = input('number: ')
nos = raw_input('bhai numbers dal space marke: ')
nos = nos.split(' ')
nos = map(int,nos)
print 'numbers hai: ',nos 
maxy = nos[0]
max2 = nos[1]
for i in nos:
    if i >= maxy:
        maxy = i
for k in nos:
    print k
    if k < maxy and k >= max2:
        max2 = k
print 'maxy number: ',maxy
print 'second largest number: ',max2
