arr = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]
'''
for i in xrange(6):
    arr_temp = map(int,raw_input('no: ').split(' '))
    arr.append(arr_temp)
'''

lst = []
for i in range(4):
  for j in range(4):
       tp_var = arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]
       print tp_var," : ",sum(tp_var)
       lst.append(sum(tp_var))
print lst
print sorted(lst)[-1]
#print "largest sum in 2D array: ",sorted(lst)[-1]
