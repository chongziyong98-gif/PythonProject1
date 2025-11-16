import random

#scenario 1: within 100, find values that can be divided by 3 or 5

items = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
print(items)

#scenario 2: in the given list of num1, create new list num2 which store values for square root of num1
num1 = [4,9,16,25,36,49,64,81]
num2 = [num**0.5 for num in num1]
print(num2)

#scenario 3: in the given list of nums1, create new list nums2 which store values for nums1 which is greater than 50
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

#To keep 3 coursework marks for 5 students respectively
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0]) #outcome is [95, 83, 92]
print(scores[0][1]) #outcome is 83

#If wish to input manually or make random, use below formula
score_list = []
for _ in range (5):
    students = []
    for _ in range(3):
        score = random.randrange(0, 100)
        students.append(score)
    score_list.append(students)

print(score_list)

score_list = [[random.randrange(0,100) for _ in range(3)] for _ in range(5)]
print(score_list)


#scenario 4: Singapore Toto Lottery

import random

print("\nWelcome to Singapore Toto Bet System, the below is the winning numbers.")
winning_numbers = sorted(random.sample(range(1, 50), 6)) #random.sample(random content, take out how many times)

remaining = set(range(1,50)) - set(winning_numbers) #use set of 1-50 minus set of winning_numbers
additional_number = random.choice(list(remaining)) #random.choice is for taking one of the value from the list. So have to convert remaining by list()

print(" ".join(f"{n:02d}" for n in winning_numbers)) #use space " ".join to join n with space (origin: n for n in winning numbers
print(f"{additional_number:02d}")




