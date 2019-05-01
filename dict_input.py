cars = {}
#while True:
for i in range(3):
 k = raw_input('enter name of car manufacturer: ')
 v = raw_input('enter the car name: ')
 cars[k] = v
print cars

print cars.keys()
print cars.values()
