class Pycharm:
    def execute(self):
        print("Code compile")
        print("Code execute")


class Laptop:
    def code(self, ide):
        #What matters is only the ide has execute method
        ide.execute()


ide = Pycharm()
lap = Laptop()
lap.code(ide)
