import threading
import time

# global variables are able to access means it shares data
results = []


def square_area(numbers):
    print("calculating square area")
    for i in numbers:
        time.sleep(0.2)
        results.append(i*i)
        print("square : " + str(i * i) )


def cube_area(numbers):
    print("calculating cube area")
    for i in numbers:
        time.sleep(0.2)
        results.append(i*i*i)
        print("cube : " + str(i * i * i) )


t = time.time()
array = [2, 3, 4, 5, 6, 34, 43]
t1 = threading.Thread(target=square_area , args=(array,))
t2 = threading.Thread(target=cube_area , args=(array,))
# start the thread
t1.start()
t2.start()

# wait until the thread is over
t1.join()
t2.join()

# square_area(array)
# cube_area(array)
print("main is done in ", (time.time() - t))
print(results)