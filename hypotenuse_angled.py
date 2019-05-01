# -*- coding: utf-8 -*-
import math
ab = input('ab side dal chal: ')
bc = input('bc sid dal chal: ')
hypo = math.sqrt((ab**2) + (bc ** 2))
print 'hypo: ',hypo
mc = (hypo/2)
x = (mc/bc)
print 'sin theta as x: ',x
sininv = math.asin(x)
print 'sin inverse',sininv
deg = math.degrees(sininv)
ds = u'\N{DEGREE SIGN}'
print 'degree: ',deg
print 'degree bole toh: ',int(math.ceil(deg)),ds
