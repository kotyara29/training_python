class Student:
    stdCount = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.stdCount += 1

    @staticmethod
    def student_count():
        print("Total Students count %i" % Student.stdCount)

    def display_student(self):
        print("Name : ", self.name, ", Age : ", self.age)

    def exam(self, new_grade):
        self.grade = new_grade


Anton = Student("Anton", 18, 69)
print(Anton.grade)
Anton.exam(77)
print(Anton.grade)
