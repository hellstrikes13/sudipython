import sys
def print_2(*args):
 arg1,arg2 = args
 print "arg1: %r  arg2: %r" %(arg1,arg2)
def print_2_again(arg1,arg2):
 print "arg1: %r  arg2: %r" %(arg1,arg2)
def print_1(arg1):
 print "arg1: %r " %(arg1)
def print_none():
 print 'i got nothing'

print_2("sudeep","melekar")
print_2_again("subhash","melekar")
print_1("hollaaaaaaa")
print_none()
