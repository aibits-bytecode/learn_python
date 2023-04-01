import time
import multiprocessing
import sys

results = []

def square_area(numbers):
    print("calculating square area")
    global results
    for i in numbers:
        time.sleep(0.2)
        results.append(i*i)
        print("square : " + str(i * i))


def cube_area(numbers):
    print("calculating cube area")
    global results
    for i in numbers:
        time.sleep(0.2)
        results.append(i*i*i)
        print("cube : " + str(i * i * i))


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    p1 = multiprocessing.Process(target=square_area, args=(arr,))
    p2 = multiprocessing.Process(target=cube_area, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("main process done")
    print(results)