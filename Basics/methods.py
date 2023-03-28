class Student:
    school = "Pythons"

    # constructor
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

        # Instance methods which use instance variables

    def get_m1(self):
        return self.m1

    # Class methods
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static method not using instance or class variables
    @staticmethod
    def info():
        print("Welcome to static method")


s1 = Student(10, 12, 13)
print(Student.getSchool())
Student.info()




