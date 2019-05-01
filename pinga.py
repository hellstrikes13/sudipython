import subprocess
urls = ['localhost','google.com','amazon.in']
lst = []
for i in urls:
    p1 = subprocess.Popen(['ping','-c4',i],stdout=subprocess.PIPE).communicate()[0].split(',')[2]
    print i,p1
