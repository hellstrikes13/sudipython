import time

startnumber = 1
endnumber = 100

# solution A without a for loop
start_time = time.clock()
m = map(str, range(startnumber, endnumber + 1))
print(' '.join(m))
end_time = time.clock()
timetaken = (end_time - start_time) * 1000
print('took {0}ms\n'.format(timetaken))

# solution B: with a for loop
start_time = time.clock()
for i in range(startnumber, endnumber + 1):
    print(i, end=' ')
end_time = time.clock()
timetaken = (end_time - start_time) * 1000
print('\ntook {0}ms\n'.format(timetaken))
