print '\nfibo series:'
cube = lambda x: x ** 3
def fibon(n):
    lst = [0,1]
    for i in range(2,n):
        lst.append(lst[i-2]+ lst[i-1])
    return(lst[0:n])

if __name__ == '__main__':
    n = int(raw_input('range of nos: '))
    print map(cube, fibon(n))

