v = input('enter the element whose index u wanna search: ')
n = input('size of array elements: ')
e = map(int,raw_input('elements').split(' '))
for i in e:
    if i == v:
        print e.index(i)
