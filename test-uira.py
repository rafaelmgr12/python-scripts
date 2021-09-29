from concurrent.futures import ThreadPoolExecutor
import threading
import random
import time
def task():
    print("Executing our Task")
    result = 0
    i = 0
    for i in range(100000000):
        result = result + i
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))

def main():
    start_time = time.time()
    executor = ThreadPoolExecutor(max_workers=6)
    task1 = executor.submit(task)
    #task2 = executor.submit(task)
    end = time.time()
    print("Task Parallel Executed in {} seconds".format(end - start_time))
    start = time.time()
    task()
    end = time.time()
    print("Task Serial Executed in {} seconds".format(end - start_time))

if __name__ == '__main__':
    main()