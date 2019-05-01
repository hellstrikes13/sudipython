from __future__ import division
n = input('no of plants: ')
ht = raw_input('ht of plants: ')
htt = set(map(int,ht.split()))
k = len(htt)
print 'total plants now: ',k
su = sum(htt)
print 'sum is: ',su
av = su / k
print 'av: ',av

