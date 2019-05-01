tc = int(raw_input(''))
for i in range(tc):
    a,b = raw_input('').split(' ')
    try:
        print int(a) / int(b)
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e
