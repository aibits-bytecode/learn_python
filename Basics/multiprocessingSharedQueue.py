import multiprocessing
import time


def square_area(numbers, que):
    print("inside the square_area function")
    time.sleep(0.2)
    for n in numbers:
        que.put(n*n)
        print("square : ", str(n * n))


if __name__ == "__main__":
    print("insidde main function")
    numbers = [3,2,3,4,5]
    q1 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=square_area, args=(numbers, q1))

    p1.start()
    p1.join()

    print("inside main function")

    while q1.empty() is False:
        print(q1.get())