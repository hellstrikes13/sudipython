bikes = {}
for i in range(3):
 kv = raw_input("enter the manu and name of bike: ")
 k = kv.split(" ")[0]
 v = kv.split(" ")[1]
 bikes[k] = v
print bikes.keys()
print bikes.values()
