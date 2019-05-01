n = [i for i in range(1,6)]
sq = [ i*i for i in n ]
print n
print sq
'''
populate list with 2 values nested list
'''
n = int(input('total nu: '))
marksheet = [[raw_input('name: '), float(input('marks'))] for _ in range(n)]
print marksheet
