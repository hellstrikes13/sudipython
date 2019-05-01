t = int(raw_input('no of testcases: '))
lst = []
lst2 = []
for i in range(t):
    s = raw_input('enter a string: ')
    for i in range(len(s)):
        if i % 2 == 0:
            lst.append(s[i])
        else:
            lst2.append(s[i])
    print ''.join(lst),''.join(lst2)
    lst[:] = []
    lst2[:] = []
