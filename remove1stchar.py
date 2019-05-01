def filter(oldfile,newfile):
  rf = open(oldfile,'r')
  wf = open(newfile,'w')
# print rf.readline()
  while True:
    text = rf.readline()
    if len(text) == 0:
     break
    if text[0]== "#":
     continue
    wf.write(text)
  rf.close()
  wf.close()
filter('apache2.conf','apache2_new.conf')
