class Vehicle:
    def __init__(self,category,wheels):
        self.category = category
        self.wheels = wheels
    def Vehdisp(self):
        return self.category , ' : ',self.wheels

class Bike(Vehicle):
    def __init__(self,category,wheels,speed):
        Vehicle.__init__(self,category,wheels)
        self.speed = speed
    def Bikdisp(self):
        return self.category ,' : ' , self.wheels ,' : ' ,self.speed

v = Vehicle('vehicle','100')
b = Bike('honda','2','200mph')
print(v.Vehdisp())
print(b.Bikdisp())
