n = int(raw_input('no of students: '))
mydict = {}
for line in range(n):
    info = raw_input('name: ').split(" ")
    score = map(float, info[1:])
    mydict[info[0]] = sum(score) / float(len(score))

print "score hai : %.2f" % round(mydict[raw_input()],2) 
