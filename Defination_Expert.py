#def can be used with def (Like if,if;for for)

import random
import time
from functools import wraps #Important!!

def record_time(func):
    @wraps(func) #Copy the decorated item, so that it wouldn't replace original defined function
    def wrapper(*args, **kwargs): #important: must use (*args, **kwargs), if use (), it will become wrapper(func), caused error
        start = time.time() #record time for start (in front of result)
        result = func(*args, **kwargs) #same goes to here
        end = time.time()
        print(f'{func.__name__} in {end - start:.2f} second')
        return result
    return wrapper

@record_time # @definition function mean record_time(download). @function is built-in
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6) #sleep mean let system wait. random.random()*6 mean random within 6 second
    print(f'{filename}下载完成.') #No need to return (return None by default), we just want to print when use this function

@record_time #record_time(upload)
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('movie.avi')
upload('Python_learning_100_days.pdf')

#question: I am now want to download but dun want to see download time, how?
#to use .__wrapped__ function, we have to use functools wraps, and put @wraps before decoration (copy wrapped version)
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')


#learning point 2: we can def a function which return defined def: example:Def(num) = num*def(num-1)
def fac(num):
    if num in (0, 1): #can also write as num == 0 or num == 1
        return 1
    return num * fac(num - 1)

print(fac(5))
#it do: 5*fac(5-1), 5*4*fac(4-1), 5*4*3*fac(3-1), 5*4*3*2*fac(2-1), 5*4*3*2*1 (return 1)

#do a,b = b, a+b
def fib1(num):
    if num in (1, 2):
        return 1
    return fib1(num - 1) + fib1(num - 2)

