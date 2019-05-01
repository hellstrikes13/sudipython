#t1 =  ''.join(map(str,range(1,input('number ')+1)))
n = input('number ')
nos =  raw_input('number dal te jaa ') 
k = []
for i in nos.split(' '): k.append(int(i))
print hash(tuple(k))
