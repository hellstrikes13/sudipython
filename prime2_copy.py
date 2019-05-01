for num in range(2,5):
# print '\nouterloop num: ',num
 prime = True
 for i in range(2,num):
 # print '\ninnerloop i: ',i
  if num % i == 0:
  # print 'num: mod  i ',num,i
   prime = False
 if prime:
   #print '\nprinting prime numbers of num'
#   print '\n ' 
   print num ,
