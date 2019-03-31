# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance Dog’s can be to print ‘voff voff’, while Cat’s can be to print ‘meow’


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        return "voff voff"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        return "meow"


pet_1 = Dog("Habby")
pet_2 = Cat("Barsik")

print(pet_1.say())
print(pet_2.say())


#####


class Pet:
    def __init__(self, name):
        self.name = name

    def say(self):
        return f'My name is {self.name}'


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'Waw, my name is {self.name} and breed is {self.breed}'

class Cat(Pet):
    def __init__(self, name, breed, colour):
        super().__init__(name)
        self.breed = breed
        self.colour = colour

    def say(self):
        return f'Meau, my name is {self.name} and breed is {self.breed}, and I have a {self.colour} colour'


pet_1 = Dog("Habby", "labradour")
pet_2 = Cat("Barsik", "british", "grey")

print(pet_1.say())
print(pet_2.say())