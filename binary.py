a='010101'
b='101101'
res = 0
for i in range(len(a)):
 if (a[i] == '1' and  b[i] == '1') or (a[i] == '0' and b[i] == '0'):
     res += 1
 else:
     pass
print res
