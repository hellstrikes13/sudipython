line, target = [raw_input('1st string 2nd substring: ') for _ in range(2)]
score = 0
for i in range(len(line)):
   if line[i:i+len(target)] == target:
        score += 1
print score
