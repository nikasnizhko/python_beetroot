
# Task.1 Exclusive common numbers

import random

list_1 = [random.randint(1, 10) for x in range(0, 10)]
list_2 = [random.randint(1, 10) for x in range(0, 10)]

print(list_1)
print(list_2)

list_3 = set(list_1).intersection(list_2)

print(list_3)




# Task.2 Extracting numbers

list = list(range(1,101))
print(list)

new_list = [number for number in list if number % 7 == 0 and number % 5 != 0]

print(new_list)

