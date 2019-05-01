import sys
a = [1,4,5,7,9,12]
min = 0
max = len(a) - 1
el = 4
print '****Binary Search****\nelements:',a,'\nelement to be searched:',el
while (min <= max):
     mid = int((min + max )/ 2)
     print 'mid value: ',mid
     if a[mid] == el:
         print 'element',a[mid],' found at: ',mid,'th location'
         sys.exit(1)
     elif a[mid] < el:
         print ' discard left'
         min = mid + 1
         print 'min value: ',min
     else:
         max = mid -1 
         print 'discard right'
         print 'max value: ',max
