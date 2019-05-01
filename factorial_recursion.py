import sys
def facto(n):
    if n == 1:
        return 1
    elif n < 1:
        print 'GL'
        sys.exit(1)
    else:
        return n * facto(n-1)
print facto(5)
