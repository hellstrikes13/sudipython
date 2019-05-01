print 'program accepts height less than 23'
while True:
 ht = input('height:')
 if ht >= 23:
     continue
 else:
     for i in range(1,ht+1):
      print " " * (ht - i)  + "#" * i + " " + "#" * i + " " * (ht - i)
     break


