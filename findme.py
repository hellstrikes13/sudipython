def findme(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            print ix
        ix += 1
    return -1
findme('sudeep','e',2)
