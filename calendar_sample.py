import calendar as c
from datetime import datetime as dt
nw = dt.now()
yr = nw.year
mnt = nw.month
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dm = {}
nos = []
dys = []
for i in c.monthcalendar(yr,mnt):
    k=0
    for d in i:
#            print d , '-> ',days[k]
            dm[d] = days[k]
            k = k+1
#print 'print dictionary'
dm.pop(0)
'''
for i in dm:
    nos.append(i) 
    dys.append(dm[i])
print 'printing nos',nos
print 'print days',dys
'''
for i in dm:
    if i % 6 == 0 or i % 7 == 0:
        print i ,'=>', "sutti "
    else:
        print i,'--> '
