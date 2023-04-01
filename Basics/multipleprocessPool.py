# by using pool we can get the work done on multiple cores
import multiprocessing
import time
from functools import partial
from itertools import product
from multiprocessing import Pool


def sum_square(a):
   print(a)


if __name__  == "__main__":
    t1 = time.time()
    p = Pool()
    p.map(sum_square, range(100))
    p.close()
    p.join()
    print("pool time : ", (time.time()-t1))

    t2 = time.time()
    sum1 = 0
    for i in range(100):
        print(i)
    print("main core time : ", (time.time()-t2))