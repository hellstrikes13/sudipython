from collections import Counter
shoes = input('no of shoes: ')
shoe_size = [ int(i) for i in raw_input('shoe size: ').split(' ')]
cust = input('no of customers: ')
ss = Counter(shoe_size)
mon = 0
print ss
purchase = []
for i in range(cust):
    profit = map(int,raw_input('size and price: ').split(' '))
    if profit[0] in shoe_size:
     shoe_size.remove(profit[0])
     mon = mon + profit[1]
print 'total money: ',mon
