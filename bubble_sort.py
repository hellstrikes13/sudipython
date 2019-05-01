def bubble(lst):
   try:
       for i,v in enumerate(lst):
           if a[i] > a[i+1]:
              a[i],a[i+1] = a[i+1],a[i]
   except:
       pass
   return lst
a = [14,10,27,33,35]
print 'orignal list is: ',a,
k = bubble(a)
print ' '
print 'sorted list is: ',k,
