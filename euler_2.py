tc = input('no of testcases: ')
for i in range(tc):
 print sum([ i for i in range(input('enter a number: ')) if i % 3 == 0 or i % 5 == 0 ])
