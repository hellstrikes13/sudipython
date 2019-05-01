t = input('no of testcases: ')
phdir = {raw_input('name: '):input('phone: ') for i in range(t)}
print phdir
name = raw_input('enter the name in phone directory: ')
for i in range(t):
 min = 0
 max = len(phdir) - 1
 el = raw_input('enter name u wanna search: ')
 while (min <= max):
     mid = int((min + max )/ 2)
     print 'mid value: ',mid
     if a[mid] == el:
         print el+'='+phdir[el]
         sys.exit(1)
     elif a[mid] < el:
     #    print el+'='+phdir[el]
         min = mid + 1
     else:
         max = mid -1 
         print 'Not found'
