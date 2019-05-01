import re
def run_re():
 pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
 rc = re.compile(pattern)
 f = open('ips','r')
 match_count = 0
 line_count = 0
 for line in f:
#   print line,
   match = rc.search(line)
   if match:
   	match_count += 1
   line_count += 1
 return(line_count,match_count)
if __name__ == '__main__':
 line_count,match_count = run_re()
 print 'lines:\t',line_count
 print 'matches:\t',match_count

