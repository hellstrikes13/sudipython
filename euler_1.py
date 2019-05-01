tc = input('no of testcases: ')
total = []
for  i in range(tc):
 k = input('enter number: ')
 for q in range(1,k):
  if q % 3 == 0 or q % 5 == 0:
   total.append(q)
#   print total
 print sum(total)
 total = []
