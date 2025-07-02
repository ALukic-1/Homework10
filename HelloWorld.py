import math
from abc import ABCMeta, ABC, abstractmethod

#a.)
print("Hello World!")

# b.)

class Student:
    def __init__(self, name,age):
        self_name = name
        self_age = age


# c.)
for i in range (10):
    print(i)


# d.)

class Shape (ABC):
    @abstractmethod
    def getArea(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius**2 * math.pi


# e.)

class Student():
    def __init__(self, name):
        self.name = name
        self.grade = {}


    def setGrade(self,course, grade):
        self.grade[course] = grade

def getAverageGrade(self):
    sum = 0
    if not self.grade:
        return 0
    for g in self.grade.values():
        sum += g
    return sum / len(self.grade)