class Area(object):
 def disp(self):
  print 'area of : ' 
class Rectangle(Area):
 global areas
 def calc_r(self,l,b):
   self.l = l
   self.b = b
   areas = l * b
   print 'Rectangle %r'%areas
class Triangle(Area):
 def calc_t(self,b,h):
  self.b = b
  self.h = h
  areas = 0.5 * b * h
  print 'Triangle %r' %areas
r = Rectangle()
t = Triangle()
r.disp()
r.calc_r(20,5)
t.disp()
t.calc_t(5,15)
