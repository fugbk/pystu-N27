# encoding = utf-8
__author__ = "Ang Li"



class Person:
    age = 10
    def __init__(self, name):
        self.name =name
        print(1, id(self))

    def showage(self):
        print(2, id(self))
        return "{} is {}".format(self.name, self.age)


tom = Person("Tom")

print(3, id(tom))
tom.showage()