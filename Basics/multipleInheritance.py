class Father:
    def work(self):
        print("I love working")

    def speaks(self):
        print("I speak english")


class Mother:
    def cooking(self):
        print("I love cooking")

    def speaks(self):
        print("I speak tamil")


class Child(Father, Mother):
    def learning(self):
        print("I love learning")

    def speaks(self):
        Father.speaks(self)
        Mother.speaks(self)


c = Child()
c.speaks()
