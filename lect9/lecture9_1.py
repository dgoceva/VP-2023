class Student:
    class_data = 3  # static data

    def static_method():  # static method
        print(Student.class_data)

    def __init__(self):
        self.instance_data = 1

    def instant_method(self, data):
        self.instance_data = data

    def __str__(self):
        return 'data: '+str(self.instance_data)

    def __repr__(self):
        return self.__str__()


print(Student.class_data)
object = Student()
print(object.instance_data)
Student.static_method()
object.instant_method(4)
print(object.instance_data)
print(object)
