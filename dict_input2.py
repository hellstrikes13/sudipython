phdir = {}
for i in range(3):
    k = raw_input('Name and phone number: ').split(' ')
    phdir[k[0]] = k[1]
print phdir
for k in phdir:
    name = raw_input('enter the name in phone directory: ')
    if name in phdir:
        print name+'='+phdir[name]
    else:
        print 'GL'
