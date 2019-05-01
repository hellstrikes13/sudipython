#try:
ar = []
a=[2,4,6,8,3]
print 'orginal a : ',a
for s in range(1,6):
     for i,v in enumerate(a):
         if a[i] == a[-1]:
             pass
         elif a[i] < a[i+1]:
   #          ar.append(v)
         else:
   #          print 'index loc: ',i
   #          ar.append(v)
    #         arindex = a.index(i)
    #         print 'arth index : ',arindex
    #         ar.insert(arindex,v)
    #         print 'ar: ',ar 
    #         ar = []
             c1,c2= a.index(a[i]),a.index(a[i+1])
             a[c2],a[c1] = a[c1],a[c2]
             print 'modified a: ',a
     print 'tik tik: ',s   
     print "--" * 10
#except:
#    print ' last element reached'
