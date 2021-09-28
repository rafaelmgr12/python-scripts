import random
import threading
import time
def timer_func(func):

    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution."
        print(msg.format(func = func.__name__,time = runtime))
        return value
    return function_timer

@timer_func
def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a 
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":
    size = 100000000   # Number of random numbers to add
    threads = 2   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    list_append(size, 8, [])

    print ("List processing complete.")