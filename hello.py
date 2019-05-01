import time
def greet():
 print 'hey der..\n whats up ??'
 print "=$=" * 10
def bye():
 '''
 this function is used to say good bye
 gl meaning is get lost
 i m sarcastically saying that..
 dont take me so seriously
 u should have lil bit of fun while programming
 isnt it fella ????
 '''
 print 'pleasure meeting u at this time: %r'%time.time()
 print 'GL now..'
def main():
 greet()
 bye()
if __name__ == "__main__":
 main()
