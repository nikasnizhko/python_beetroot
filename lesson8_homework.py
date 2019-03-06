# # Task.1   A simple function

def favourite_movie():
    name = input("What is your favourite movie? ")
    return "My favourite movie is " + str(name)

my_movie = favourite_movie()
print(my_movie)


# # Task.2 Creating a dictionary


from typing import Dict

def make_country(name: str, capital: str) -> Dict:
    country = {"name": name, "capital": capital}
    return country
    #return country.values()


countries = make_country(name="Brazil",capital="Brasilia")
print(countries.values())



# Task.3 A simple calculator.


def make_operation(operator: str, *args: int) -> int:
    result = args[0]
    for number in args[1:]:
        if operator == "+":
            result += 1               #return sum(args)
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        else:
            print("Use other operator")
            break
    return result


print(make_operation("-", 5, 5, -10, -20))
