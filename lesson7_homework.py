#Task.1 Dict comprehension exercise.


user_input = input("Enter your text: ")
text = user_input.split()

new_dict = {word: text.count(word) for word in text}
print(new_dict)



#Task.2 List comprehension exercise I


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number%2 != 0]

print(b)


#Task.3 List comprehension exercise II


list_1 = [(i,i**2) for i in range(1,11)]
print(list_1)



