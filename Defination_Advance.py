# Defining can return the defined function as result

def cal(initial,oprt_cal,*args,**kwargs):
    items = list(args) + list(kwargs.values())
    result = initial
    for item in items:
        if type(item) in (int,float):
            result = oprt_cal(result,item)
    return result

def add(a,b):
    return a+b
def mul(a,b):
    return a*b

print(cal(1,mul,2,4,5))

#map,filter mean map(for all fulfilled number), filter (further fulfilled)
#it is same as (i for i in list if i...) something
#lambda = anonymous function (used if the function very simple)

old_number = [2,6,13,25,34]
new_number = list(map(lambda x:x**2,filter(lambda x:x%2==0,old_number)))
print(new_number)

#With lambda, we can use one line to calculate is_prime
is_prime = lambda x: all(map(lambda f:x%f,range(2,int(x**0.5)+1)))
print(is_prime(5))
#Short explain = to find out bool of x (First Lambda).
#all() = will return bool if there is not 0 , 0.0 , "" , {}, (), [] otherwise, if any of the value inside, will return False
#Second lambda = for every f, execute x%f.
#Map mean f (in the range set) will execute x%f and put into list. If there is 0, return False
