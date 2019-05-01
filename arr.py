n = 5
arr = [1,2,3,4,5]
arrs = sum(arr)
print 'sum of original arr: ',arrs
print (arrs/n)+1
'''
#mins  =  []
for i in sorted(arr):
    print 'array ele: ',i
    temparrs = sum([i for x in range(n)])
    print 'temp array sum     :',temparrs
    print 'original array sum :',arrs
    if temparrs > arrs:
#        mins.append(i)
        print 'got the element bye',i
        break
    else:
        print 'condition not met'
        pass
#print 'minimum arrary element: ',min(mins)
'''
