from numba import jit,njit, prange
import random
import time 
import numpy as np
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




def monte_carlo_pi_2(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

@jit(nopython=True, parallel=True,nogil=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in prange(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
if __name__ == "__main__":
    start = time.time()
    monte_carlo_pi_2(100000000)
    end = time.time()
    print("Time taken for monte_carlo_pi_2: ", end - start)	
    start = time.time()
    monte_carlo_pi(100000000)
    end = time.time()
    print("Time taken for monte_carlo_pi: ",end-start)