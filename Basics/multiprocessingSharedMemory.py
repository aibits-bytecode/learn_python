import time
import multiprocessing


def square_area(numbers, results, v):
    print("calculating square area")
    v.value = 20
    for idx, n in enumerate(numbers):
        time.sleep(0.2)
        results[idx] = n*n
        print("square : " + str(n * n))


def cube_area(numbers):
    print("calculating cube area")
    for i in numbers:
        time.sleep(0.2)
        results.append(i*i*i)
        print("cube : " + str(i * i * i))


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    # creating a shared memory
    # 1st argument is data type
    # 2nd argument is how many elements
    # shared memory access is different so we have to access by index
    results = multiprocessing.Array("i", 4)
    value = multiprocessing.Value("i", 10)
    p1 = multiprocessing.Process(target=square_area, args=(arr, results, value))
    #p2 = multiprocessing.Process(target=cube_area, args=(arr,))

    p1.start()
    #p2.start()

    p1.join()
    #p2.join()

    print("main process done")
    print(results[:])
    print(value.value)