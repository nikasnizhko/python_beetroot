#Task.1 The valid phone number

number = "55795788g6"

if len(number) == 10 and number.isdigit():
    print("Number is correct")
else:
    print("The phone number is not correct")

#Task.2 The math quiz program

print("24 * 4 = ?")
user_answer = input("What is the answer?")
if user_answer == str(24*4):
    print("Great! You should be a scientist!")
else:
    print("Try one more time")


#Task.3 The name check

name = "nika"
user_input = input("What is your name?")
if user_input.lower() == name:
    print(True)
else:
    print(False)