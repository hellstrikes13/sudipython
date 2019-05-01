class Area(object):
 def calc(self,a,b):
   self.a = a
   self.b = b
class Rectangle(Area):
 def calc():
   super(Area,self)
   areas = a * b
   print 'Area of Rectangle %r'%areas

class Triangle(Area):
 def calc():
  super(Area)
  areas = 0.5 * b * h
  print 'Area of Triangle %r' %areas
r = Rectangle()
t = Triangle()
r.calc(20,5)
t.calc(5,15)
