from __future__ import division
#import collections
no_of_stud = input('no of studs: ')
students = {}
#students = collections.OrderedDict()
for i in range(no_of_stud):
   name_marks = raw_input('name and marks: ')
   names = name_marks.split(' ')
# populate keys in dictonary
   i = names[0] 
# populate values in dictonary
   students[i] = names[1:] 
#print students

#last_name = list(students)[-1]
person_name = raw_input('Person name: ')


marks = students[person_name]
print marks
total = 0
for k in marks:
  total = total + float(k)
avg_marks = total / len(marks)
print 'bhaya tera avg marks yeh hai: %.2f'%(avg_marks)
