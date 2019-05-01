print 'program accepts height less than 23'
while True:
 ht = input('height:')
 if ht >= 23:
     continue
 else:
     for i in range(2,ht):
      print " " * (ht - i)  + "#" * i
     break


