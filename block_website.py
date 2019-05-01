import time
from datetime import datetime as dt
hosts = "/etc/hosts"
redirect = "127.0.10.100"
websites = ['www.facebook.com','facebook.com']
d = dt.now()
while True:
    if dt(d.year,d.month,d.day,21) < d < dt(d.year,d.month,d.day,22):
        print 'working hours !!!'
        with open("/tmp/hosts",'r+') as f:
            content = f.read()
            for i in websites:
                if i in content:
                    pass
                else:
                    f.write(redirect+' '+i+"\n")
    else:
        print 'fun hours...'
        with open("/tmp/hosts",'r+') as file:
                con = file.readlines()
                print con
                file.seek(0)
                for line in con:
#                   print line
                    if not any( webs in line  for webs in websites):
#                        print 'writing this line',line
                        file.write(line)
                    else:
                        print 'i wont write this line',line
                file.truncate()
    time.sleep(5)
        
        
        
        



