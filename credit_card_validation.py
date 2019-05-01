nos = []
while True:
    cr = raw_input('enter credit card number: ')
    if len(cr) > 16 or len(cr) < 16:
        print 'INVALID'
        continue
    else:
        for e,i in enumerate(cr,start=1):
            if e % 2 == 0:
                nos.append(i)
        print nos
        break
