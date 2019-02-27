#Task.1 The Guessing Game.

import random

while True:
    d = int(input("input any number in range 1-5: "))
    e = random.randint(1, 10)
    if d != e:
        print("Try harder! The correct number is ", e)
        continue
    else:
        print("Good Job!")
        break


#Task.2 The birthday greeting program.


user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_age += 1
print (f"Hello {user_name}, on your next birthday you'll be {str(user_age)} years")
