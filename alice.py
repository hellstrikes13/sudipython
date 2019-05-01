alice = map(int,raw_input("alice 3 elements: ").split(' '))
bob = map(int,raw_input("bob 3 elements: ").split(' '))
als = sum([1 for a,b in zip(alice,bob) if a > b])
bos = sum([1 for a,b in zip(alice,bob) if b > a])
print 'score: ',als , bos
