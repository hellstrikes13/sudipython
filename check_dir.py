import os
import sys
di = sys.argv[1]
if os.path.isdir(di):
 print 'yes %r is directory'%di
else:
 print ' %r is not a directory'%di
