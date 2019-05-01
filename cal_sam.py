from datetime import datetime as dt
import calendar as cl
nw = dt.now()
yr = nw.year
mnt = nw.month
dm = {}
day_nos = []
days = ['Monday]
for i in cl.monthcalendar(yr,mnt):
      k=0
      for d in i:
        dm[d] = days[k]
        k+=1
print dm
'''
dm.pop(0)
for i in dm:
       day_nos.append(i) 
       days.append(dm[i])
  
values = []
values.append(day_nos)
values.append(days)
print values
'''
