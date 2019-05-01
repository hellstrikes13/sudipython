'''
this program illustrates usage of decorate division
for 2/0 divide by 0 exception a decorator is used to raise this error in 
human form
and also general use-case of Decorators...
'''

def divi(func):
    def inner(a,b):
        print 'dividing number1 / number2'
        if b == 0:
            print 'sorry BOSS !! i cannot divide anything by 0 ; BC dont put 0 as divisor'
            return
        return func(a,b)
    return inner

@divi
def divideme(a,b):
    return a/b
print divideme(input('number 1: '),input('number 2: '))


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

def star(func):
    def inner(*args,**kwargs):
        print '*' * 30
        func(*args,**kwargs)
        print '*' * 30
    return inner

@star
@percent
def hello(msg):
  print msg
hello('hiiii')

