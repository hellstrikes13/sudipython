f = open('movi','r')
data = f.readlines()
data2 = map(lambda s:s.strip(),data)
a,b=0,5
x = open('movi.csv','w') 
while(a<len(data2)):
    print ','.join(data2[a:b])
    x.writelines(','.join(data2[a:b])+'\n')
    a += 5
    b += 5
f.close()
x.close()
