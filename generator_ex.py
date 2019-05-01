gen = ( x for x in range(1,11))
print gen
for i in gen:
  print i
a= [x for x in range(1,11)]
print "-||-"*10
def PowTwoGen(max = 0):
  n = 0
  while n < max:
    yield 2 ** n
    n += 1
x =  PowTwoGen(input('Enter no. range to get POWER OF 2s: '))
for i in x:
    print i
