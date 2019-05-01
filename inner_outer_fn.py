def outer():
     def inner():
         print "Inside inner"
     return inner # 1
     print "outer function"
     return outer
'''
foo = outer()
print foo() 
'''
