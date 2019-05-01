s = ['s','u','d','e','e','p']
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
	print '%s comparing with %s so result is yes' %( s[i] , s[i +1])
    else:
        print '%s comparing with %s so result is no' %( s[i] , s[i +1])
