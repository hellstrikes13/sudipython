def quicksort(listtosort,lowindex,highindex):
    if ((highindex - lowindex) > 0):
        p = partition(listtosort,lowindex,highindex)
        quicksort(listtosort,lowindex,p-1)
        quicksort(listtosort,p+1,highindex)

def partition(listtosort,lowindex,highindex):
    divider = lowindex
    pivot = highindex

    for i in range(lowindex,highindex):
        if (listtosort[i] < listtosort[pivot]):
            listtosort[i],listtosort[divider] = listtosort[divider],listtosort[i]
            divider += 1
    listtosort[pivot],listtosort[divider] = listtosort[divider],listtosort[pivot]
    
    return divider
lst1 = [6, 2, 9, 8, 0, 1, 5, 7, 4, 3]
lst2 = [3, 4, 2, 9, 1, 7, 6, 5, 8, 0]
lst3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print 'before sort: ',lst1
quicksort(lst1,0,9)
print 'after sort: ',lst1
print '\n'

print 'before sort: ',lst2
quicksort(lst2,0,9)
print 'after sort: ',lst2
print '\n'

print 'before sort: ',lst3
quicksort(lst3,0,9)
print 'after sort: ',lst3
print '\n'

print 'before sort: ',lst4
quicksort(lst4,0,9)
print 'after sort: ',lst4

