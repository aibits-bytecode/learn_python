# when running the python file we can send arguments in command line
# we have 2 types
# positional arguments // they should send with the python file
# optional arguments  // it is not required to send these arguments

# run the command by follow
# python position_arguments.py  1  2  add

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)