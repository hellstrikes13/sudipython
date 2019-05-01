import re
def re_run():
 patern  = r"NetworkManager"
 f = open('/var/log/syslog','r')
 match_count = 0
 lines = 0
 for line in f:
   match = re.findall(patern,line)
   if match: 
    match_count += 1
   lines += 1
 return(lines,match_count)

if __name__ == "__main__":
 lines , match_count = re_run()
 print 'LINES:',lines
 print 'MATCHES:',match_count

 
