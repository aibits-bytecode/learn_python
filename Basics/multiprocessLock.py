import multiprocessing


def deposit(acc_balance, dep_ammount,lock):
    lock.acquire()
    acc_balance.value = acc_balance.value + dep_ammount
    lock.release()


def withdraw(acc_balance, wid_ammount, lock):
    lock.acquire()
    acc_balance.value = acc_balance.value - wid_ammount
    lock.release()


if __name__ == "__main__":
    acc_balance = multiprocessing.Value('d', 0.0)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit, args=(acc_balance, 10000.0, lock))
    p2 = multiprocessing.Process(target=withdraw, args=(acc_balance, 5000.0, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(acc_balance.value)