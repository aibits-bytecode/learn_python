# decorator allow to wrap your function in another function
import time


def performance(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took :" + str((end - start) * 1000) + " seconds")
        return results

    return wrapper


@performance
def square_area(numbers):
    results = []
    for i in numbers:
        results.append(i * i)
    return results


@performance
def cube_area(numbers):
    results = []
    for i in numbers:
        results.append(i * i * i)
    return results


numbers = range(1, 100000)
results1 = square_area(numbers)
results2 = cube_area(numbers)
