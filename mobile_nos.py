n = input('enter total number of testcases: ')
mobis = []
for i in range(n):
    n = raw_input('enter mobile no: ')
    if len(n) == 10:
        mobis.append(n)
    elif len(n) > 10:
        mobis.append(n[-10:])
m =  sorted(mobis)
print m
for i in m:
    print "+91 ",i
