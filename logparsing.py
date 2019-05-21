import re
import sys
import time
from datetime import datetime
from pytz import timezone
'''
author: sudi
script will run only in python3
-  Counts the number of occurrences of a string provided as an argument
-  Reports the average time elapsed between occurrences of the string
-  Prints the log, but translates timestamps of each occurrence into PST (Pacific Standard Time)
'''
pat = '\[\d+\/[a-zA-z]+\/\d+:\d+:\d+:\d+\s\+0000\]'
fmt = '%d-%b-%Y:%H:%M:%S %z'
if len(sys.argv) < 2:
  print('missing command line args bhauuuuu ')
  sys.exit(1)
else:
  print('welcome dudewa...')
  search_pat = sys.argv[1]

with open('frontend-service.log','r') as f:
  data = f.read()
def pst_time():
  print('datetime changed from GMT to PST')
  for  i in data.split("\n"):
    try:
      utc =  re.search(pat,i).group(0).strip('[]')
      pst = datetime.strptime(utc,"%d/%b/%Y:%H:%M:%S %z").astimezone(timezone('US/Pacific')).strftime(fmt)
      print(i.replace(utc,pst))
    except:
      pass

def count_occurances():
  print("COUNT ",search_pat,":",data.count(search_pat))

def elapsed_time():
  start_time= time.time()
  count_occurances()
  end_time = time.time()
  print("Search pattern Elapsed time:",end_time-start_time)

if __name__ == "__main__":
  pst_time()
  count_occurances()
  elapsed_time()
