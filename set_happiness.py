total_arr_set_ele = raw_input('total array and set elements: ')
arr = raw_input('array elements: ')
a_ele = raw_input('set A: ')
b_ele = raw_input('set B: ')
happiness = 0
for i in arr:
 print i
 if i in a_ele:
  happiness += 1
  print 'happiness in a_ele ',happiness
 if i in b_ele:
  happiness -= 1
  print 'happiness in b_ele',happiness
print 'total happiness: ',happiness
