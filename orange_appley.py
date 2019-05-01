s,t = [int(i) for i in raw_input('s,t start and end point: ').split(' ')]
a,b = [int(i) for i in raw_input('a,b distance of apple and orange from the house: ').split(' ')]
m,n = [int(i) for i in raw_input('m no of apples n no of oranges: ').split(' ')]
da = map(int,raw_input('distances that each apple falls from point a: ').split(' '))
do = map(int,raw_input('distances that each orange falls from point b: ').split(' '))
apple = 0
orange = 0
'''
for k in range(m):
    print 'loop count apple ',k
    '''
for i in da:
        print 'da val: ',i
        if (a + i) >= s and (a + i) <= t:
            apple += 1
        else:
            print 'oh no'
'''
for s in range(n):
    print 'loop count orange ',s
    '''
for i in do:
        print 'do val ',i
        if (b + i) >= s and (b + i) <= t:
            orange += 1
            print 'orange now',orange
        else:
            print 'oh no'
print 'no of apples',apple
print 'no of oranges',orange


