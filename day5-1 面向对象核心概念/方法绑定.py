# encoding = utf-8
__author__ = "Ang Li"

class Person:
    def __init__(self, name):
        self.name = name
        print('init~~~~~~~~~~~~~~~~~~~~~~~~')

    def showname(self):
        print(self.name)

tom = Person('Tom')

tom.showname()

Person.showname(tom)
