studmarks = []
'''
for  i in range(input('number: ')):
    studmarks.append([raw_input('name: '),float(input('marks: '))])
print studmarks
'''
s = [['a', 123.0], ['b', 789.0], ['c', 456.0]]
print s
def getkey(item): return item[1]

print sorted(s,key=getkey)
