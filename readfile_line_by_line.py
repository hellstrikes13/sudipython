f  = open('words','r')
while True:
 lines = f.readline()
 if len(lines) == 0:
  break
 print lines
f.close()
