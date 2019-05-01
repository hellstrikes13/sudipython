from sys import argv
script , filename = argv
print "we are going to erase %r " % filename
print "if u dont wanna do that hit ctrl + c (^c)"
print "if u wanna do that then hit return/Enter key"

raw_input("? ")
print "opening the file..."
target = open(filename,'w')
print "truncating the file"
target.truncate()
print "now i m gonna ask u for 3 lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
line4 = raw_input("line4: ")
print "i m gonna write all these lines to file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")

print "finally we are closing the file..."
target.close()
