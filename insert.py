def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    print tmp
    aList[k] = tmp
  return alist
alist = [2,4,6,8,3]
s = insertionsort(alist)
print s
