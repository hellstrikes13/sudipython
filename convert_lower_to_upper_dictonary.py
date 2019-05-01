dys = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
print 'orignal dict:\n',dys
print '\nconverting values in dict from lower  to upper case\n'
dys.update([(k,v.upper()) for k,v in dys.iteritems()])
print 'After conversion:\n',dys

