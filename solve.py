import time
from joblib import Parallel, delayed

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



def countdown(n):
    while n>0:
        n -= 1
    return n


t = time.time()
for _ in range(50):
    print(countdown(10**7), end=" ")
print(time.time() - t)  
# takes ~10.5 seconds on medium sized Macbook Pro


t = time.time()
results = Parallel(n_jobs=8)(delayed(countdown)(10**7) for _ in range(50))
#print(results)
print(time.time() - t)
# takes ~6.3 seconds on medium sized Macbook Pro