# encoding = utf-8
__author__ = "Ang Li"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showage(self):
        return self.age

print(*Person.__dict__.items(), sep='\n')


