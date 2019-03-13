# Task 1. A person class


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")


person1 = Person("Carl", "Johnsn", "26")


person1.talk()


