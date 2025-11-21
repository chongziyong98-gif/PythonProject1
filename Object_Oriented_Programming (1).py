#Object, Class, Encapsulation, Inheritance, Polymorphism

#Object = the main object
#Class = Group of the object (definition)
#Encapsulation = Define a complicated action with combination of multiple action

class student:
    def __init__(self,name,age): #use __init__ to set initial (default), for classification, must start with self
        self.name = name #self.name mean take name from self
        self.age = age

    def learn(self,course):
        print(f"{self.name} is learning {course}")

    def play(self,game):
        print(f"{self.name} is playing {game}")

stu1 = student("Alvin",27) #if __init__ have 2 args, here also must have 2 respective
stu1.learn("python") #get learn (defined) from stu1, and stu1 is classified as student
stu1.play("dota") #since we apply play, play is defined as will print.

#example 2: clock

import time

class clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}" #if no return, it will keep showing None

clock = clock(23,59,50) #Suggest class "clock" be in "Clock" even it can run smooth. Avoid confusion
for _ in range(11): #if want to function like real clock, use while True
    print(clock.show()) #show() function are without print, so here use print
    time.sleep(1) #sleep mean pause how many second (we import time)
    clock.run()


