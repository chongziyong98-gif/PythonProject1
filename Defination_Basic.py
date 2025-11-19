#Dictionary

def add(*args): #We can use * inside bracket before element to support multiple input
    total = 0 #Since we allow user input multiple, we need to preset a key for return later
    for item in args:
        if type(item) in (int, float): #determine if user input are int/float
            total += item
    return total

print(add(1,2,3,4,5,6,7,8,9))
print(add(1, 2, 'hello', 3.45, 6)) #hello will be neglected from add

def foo(*args, **kwargs): #We can use (**）to allow dictionary form. If user input xx=xx，will be classified under **
    print(args)
    print(kwargs)

foo(3, 2.1, True, name='Zi Yong', age=43, gpa=4.95) #args = 3, 2.1, True . and **kwargs for those =

#Practise 1: Randomly generate code

import random
import string #This is including digits (0-10) and ascii_letter(a-z,A-Z)

ALL_CHARS = string.digits + string.ascii_letters
def generate_code(*,code_len = 4): # *make multiple input, and code_len is the length, =4 is default set as 4
    return ''.join(random.choices(ALL_CHARS, k=code_len))
for _ in range(3):
    print(generate_code())
    print(generate_code(code_len=6))

#Practise 2: Define is_prime
def is_prime(num:int)->bool:
    for i in range(2,int(num **0.5) +1 ):
        if num % i == 0:
            return False
    return True
print(is_prime(81))

#Practise 3: Singapore Toto (Advance)

def choose_winning_number():
    numbers = random.sample(range(1, 50), 6)
    return sorted(numbers)

def choose_additional_number(winning_numbers):
    remaining = set(range(1, 50)) - set(winning_numbers)
    return random.choice(list(remaining))

winning_numbers = choose_winning_number()
additional_number = choose_additional_number(winning_numbers)

print("Winning numbers:", " ".join(f"{n:02d}" for n in winning_numbers))
print("Additional number:", f"{additional_number:02d}")



