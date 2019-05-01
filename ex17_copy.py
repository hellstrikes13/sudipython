from sys import argv
from os.path import exists
script , from_file , to_file = argv
print "copying from %s to %s" % (from_file , to_file)
txt  = open(from_file,'r').read()
print "input file is %d bytes long" % len(txt)
print "does the output file exists %r " % exists(to_file)
print "ready to hit return to continue , <ctrl+c> to abort "
raw_input("> ")
fo = open(to_file,'w').write(txt)
#fo.write(txt)

print "everything's done ..."
#txt.close()
#fo.close()
