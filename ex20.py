from sys import argv
script , filename = argv
def print_all(f):
 print f.read()

def rewind(f):
 f.seek(0)

def print_a_line(line_count,f):
 print line_count , f.readline(),

fi = open(filename)

print '1st lets print the whole file: \n'
print_all(fi)
print 'now lets rewind the file'
rewind(fi)

print 'lets print 3 lines'

current_line = 1
print_a_line(current_line,fi)

current_line+=1
print_a_line(current_line,fi)

current_line+=1
print_a_line(current_line,fi)
