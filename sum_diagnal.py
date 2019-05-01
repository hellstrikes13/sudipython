n = int(raw_input('numbers: ').strip())
a = []
count = 0
d_count = 0
q = -1
for a_i in xrange(n):
    a_temp = map(int,raw_input('elements: ').strip().split(' '))
    a.append(a_temp)
    count = count + a[a_i][a_i]
    d_count = d_count + a[a_i][q]
    q = q - 1
diffy = abs(count - d_count)
print 'absolute difference between the two sums of the matrix\'s diagonals',diffy
