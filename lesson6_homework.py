# Task.1


generated_list = []

for number in range(1,101):
    generated_list.append(number*number)
print(generated_list)



# Task.2

list_of_cars = []

while True:
    user_input = input("Enter the name of the car (type q to quit): ")
    if user_input == "q":
        break
    list_of_cars.append(user_input)
print(list_of_cars)



# Task.3


list_1 = [4, 5, 6, 8, 45, 56, 76, 5, 65, 3]

print(list_1)
reversed_list = list(reversed(list_1))
print(reversed_list)
