import subprocess
import sys
host = "localhost"
cmd = "uname -a"
sh = subprocess.Popen(["ssh","%s"% host, cmd],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rs = sh.stdout.readlines()
if rs == []:
 error = sh.stderr.readlines()
 print sys.stderr,"error",error
else:
 print rs


