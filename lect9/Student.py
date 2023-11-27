import csv


class Student:
    def __init__(self, fnom, name, mark):
        self.fnom = fnom
        self.name = name
        self.mark = mark

    def __str__(self):
        return f'({self.fnom},{self.name},{self.mark})'

    def __repr__(self):
        return self.__str__()


class Group:
    def __init__(self):
        self.group = []

    def __str__(self):
        return str(self.group)

    def __repr__(self):
        return self.__str__()

    def readFromCSV(self, fname):
        with open(fname) as f:
            reader = csv.reader(f)
            for student in reader:
                try:
                    fnom = int(student[0])
                    name = student[1]
                    mark = float(student[2])
                except ValueError:
                    pass
                else:
                    self.group.append(Student(fnom, name, mark))

    def averageMark(self):
        try:
            sumMark = 0
            for student in self.group:
                sumMark += student.mark
            return sumMark/len(self.group)
        except ZeroDivisionError:
            print('No data')

    def maxMarkStudent(self):
        index = 0
        for i in range(1, len(self.group)):
            if self.group[index].mark < self.group[i].mark:
                index = i
        return self.group[index]

    def minMarkStudent(self):
        index = 0
        for i in range(1, len(self.group)):
            if self.group[index].mark > self.group[i].mark:
                index = i
        return self.group[index]

# fnom = int(input('Faculty number: '))
# name = input('Name: ')
# mark = float(input('Mark: '))
# student = Student(fnom, name, mark)
# print(student)


group = Group()
group.readFromCSV(r'lect9\students.csv')
print(group)
print(group.averageMark())
print(group.maxMarkStudent())
print(group.minMarkStudent())
