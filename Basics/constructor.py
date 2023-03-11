class Computer:
    def __init__(self):
        self.name = "Kevin"
        self.age = 30

    def update(self):
        self.age = 20

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


comp1 = Computer()
comp2 = Computer()

comp1.name = "Saman"
comp1.age = 18

if comp1.compare(comp2):
    print("Same species")
else:
    print("different species")

print(comp1.name)
