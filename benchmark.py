import random
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
def Myfunction():
    for x in range(5):
        sleep_time = random.choice(range(1,3))
        time.sleep(sleep_time)

if __name__ == '__main__':
    Myfunction()