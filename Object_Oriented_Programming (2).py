#Learn Point 1: Python allow add attribution without preset available attribute.

class Student:
# if do not with ppl to add attribute, key __slots__ = ("name","age")
    def __init__(self, name, age): #preset two attribute
        self.name = name
        self.age = age

stu = Student('王大锤', 20) #here still need 2 attribute
stu.sex = '男' #add in new attribute by using .attr = value

#learn point 2: "class" is also considered "object

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod #This is to let python know this is static method, there is another one called @classmethod
    def is_valid(self):
        return a+b>c, a+c>b, b+c>a

    @property #with property, we don't have to use Triangle.perimeter(), can use direct function
    def perimeter(self):
        return self.a+self.b+self.c
    @property
    def area(self):
        p = self.perimeter/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5


t = Triangle(3, 4, 5)
print(f'perimeter: {t.perimeter}')
print(f'area: {t.area}')

#inherit

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name} is learning {course_name}.')


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title} is teaching {course_name}.')


stu1 = Student('Alvin', 27)
stu2 = Student('Zi Yong', 25)
tea1 = Teacher('ZF', 35, ' teacher')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python')
tea1.teach('Python')
stu2.study('SQL')