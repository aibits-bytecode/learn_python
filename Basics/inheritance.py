class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is calling")

    def feature2(self):
        print("Feature 2 is calling")


class B(A):
    # if only child class does not have init it will call parent class init
    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature 3 is calling")

    def feature4(self):
        print("Feature 4 is calling")

a1 = A()
b1 = B()

b1.feature1()