from __future__ import division
no_of_stud = input("no of students: ")
students = {}
last_name = ""
'''
this for loop will populate key value pair in dictonary named as students
'''
for i in range(1,no_of_stud+1):
   name = raw_input("name: ")
   marks = raw_input("marks: ")
# adding keys in dictonary i.e name taken from stdin passed saved it as key in dict student
   i = name
# adding values in dictonary corresponding to that key
   students[i] = marks 
#retreive last entered key

last_name = list(students)[-1]
print last_name
marks = students[last_name]
m = marks.split(' ')
#print type(m)
print 'printing marks of last student: ',m

total = 0
for k in m:
#  total = total + k
  total = total + int(k)
avg_marks = total / len(m)
print 'avg marks of %s %.2f'%(last_name,avg_marks)
