class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber
class Student(Person):
    def __init__(self,firstName, lastName, idNumber,scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sc = sum(scores)/numScores
        if sc >= 90:
            ch = "O"
        elif sc >= 80:
            ch = "E"
        elif sc >= 70:
            ch = "A"
        elif sc >= 55:
            ch = "P"
        elif sc >= 40:
            ch = "D"
        else:
            ch = "T"
        return ch
'''
line = raw_input('enter name and ID: ').split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
'''
firstName = 'sudeep'
lastName = 'melekar'
idNum = 123
#numScores = input('total number of scores: ')
scores = map(int, raw_input('enter scores: ').split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
