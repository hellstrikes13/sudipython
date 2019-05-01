def selects(lst):
    for i in range(len(lst)):
            frst = i
            print '\nOUTER LOOP i: ',frst
            for k in range(i+1,len(lst)):
                print 'inner loop k: ',k
                print 'lst of k: ',lst[k],'and lst of frst i: ',lst[frst]
                print 'is', lst[k], '<' , lst[frst]
                if lst[k] < lst[frst]:
                    frst = k
            print 'SWAPPPING VALUES'
            print 'lst of i: ',lst[i],'lst of frst: ',lst[frst]
            lst[i],lst[frst] = lst[frst],lst[i]
    return lst
a = [14,10,27,33,35]
print 'orignal list is: ',a,'\n'
k = selects(a)
print ' '
print 'sorted list is: ',k,
