from sys import argv
#take 1 argument to this scipt as the file name
#script , filename = argv
filename = raw_input("filename: ")
#open the filename and store it in an file object named as 'txt'
txt = open(filename)
#print filename which u supplied as 1st cmd line argv
print "here's ur file %r" % filename
#display all the contents of file.
print txt.read()
#again do the samething above  i m just including a prompt and asking user to give another file
print 'please type the filename again'
file_again = raw_input("> ")
txt2 = open(file_again)
print txt2.read()
txt.close()
txt2.close()

