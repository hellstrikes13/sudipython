def tri(n):
 tri = 0
 count = 0 
 while count < n:
  count = count + 1
  tri = tri + count
  print "%r\t %r"%(count,tri)
tri(5)

