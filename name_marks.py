mainstud = []
stud = []
for i in range(2):
 stud.append(raw_input('name: '))
 stud.append(input('marks: '))

mainstud.extend(stud)
print stud
print mainstud

