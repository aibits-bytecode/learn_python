x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

try:
    print(x/y)
except Exception as e:
    print("Exception occured :" , e, type(e).__name__)

# more on exceptions

# how to raise exceptions
try:
    raise Exception("Exception 1")
except Exception as e:
    print(e)


# create our own exception
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("user defined exception ", self.msg)


try:
    raise Accident("crash occured")
except Exception as e:
    print("Exception occured ", e)

# finally uses to do something if exception occurs or not