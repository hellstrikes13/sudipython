import numpy
n,m = map(int,raw_input('order of matrix bol chal n x m bole toh: ').split(' '))
print n,m
mat=[]
for i in range(n):
  mat.append(map(int,raw_input('number dalte ja datpro: ').split(' ')))
print 'matrix array',mat

k = numpy.array(mat,int)
print numpy.transpose(k)
print k.flatten()

