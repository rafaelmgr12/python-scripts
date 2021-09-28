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
def list_loop():
    input_list = [random.randint(-100,100) for i in range(10000000)]
    output_list = []
    for x in input_list:
        if x >= 0:
            output_list.append(1)
        else:
            output_list.append(0)

@timer_func
def list_comphension():
    input_list = [random.randint(-100,100) for i in range(10000000)]
    output_list = [1 if x >= 0 else 0 for x in input_list]




if __name__ == '__main__':
    list_loop()
    list_comphension()
