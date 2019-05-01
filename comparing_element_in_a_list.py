numlist = [2, 2, 2, 4, 4]
for i in range(len(numlist)-1):
    if numlist[i] == numlist[i + 1]:
	print '%d comparing with %d so result is yes' %( numlist[i] , numlist[i +1])
    else:
        print '%d comparing with %d so result is no' %( numlist[i] , numlist[i +1])
