try:
    arr = []
    a = [2,4,6,8,3]
    for i,v in enumerate(a):
        print i,v
        if a[i] < a[i+1]:
         arr.append(v)
        else:
            arr.append(v)
            e = a[i+1]
    print arr
except:
    pass


