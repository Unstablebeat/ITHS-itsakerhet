## List comprehensions ##

# numbers = [1,2,3,4,5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

# numbers = [1,2,3,4,5]
# squares = [num ** 2 for num in numbers]
# print(squares)

# multiplication_table = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         multiplication_table.append(i*j)
# print(multiplication_table)

# multiplication_table = [i * j for i in range(1, 4) for j in range(1, 4)]
# print(multiplication_table)

# numbers = [1,2,2,3,4,5]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)

# fruits = ["apple", "banana", "cherry"]
# word_lengths = {fruit: len(fruit) for fruit in fruits}
# print(word_lengths)

## enumerate ##

# enumerate(fruits, start=5)

# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# text = "Python"
# for index, char in enumerate(text):
#     print(f"{index}, {char}")

# persons = [("bobbo", 24), ("alice", 25)]
# for index, (name, age) in enumerate(persons):
#     print(f"Index: {index}, Namn: {name}, Ålder: {age}")

## Zip ##

# names = ["Bobbo", "Alice", "Max", "Becka"]
# ages = [37, 25, 104]
# for name, age in zip(names, ages):
#     print(f"Namn: {name}, Ålder: {age}")

## In operator ##
# fruits = ["apple", "banana", "cherry"]
# print("pinaple" in fruits)

## Min max random ##

# nummer = [1,5,7,10,9]
# print(min(nummer))
# print(max(nummer))

# import random
# print(random.randint(1,10))

# fruits = ["apple", "banana", "cherry"]
# print(random.choice(fruits))

# nummer = [1,5,7,10,9]
# print(random.choice(nummer))

## Input ##
# name = input("Vad heter du? ")
# print(name)

## Functions ##

# def function_name(param):
#     # kodblock
#     return result

# def greet(name):
#     return f"Hej, {name}"

# print(greet("Bobbo"))

# def say_hello():
#     print("Hej")
# say_hello()

# def add(a,b):
#     return a+b

# result = add(5, 2)
# print (result)

# def greet(name="Bobbo"):
#     return f"Hej, {name}"
# print(greet())
# print(greet("Steve"))

# def pet(animal_type, pet_name):
#     print(f"{animal_type} och {pet_name}")

# pet(pet_name="Cattie", animal_type="Cat")

# result = (square(5))
# print(result)

# def square(number):
#     return number * number

# def add(a, b):
#     return a+b

# def add_and_square(a, b):
#     sum = add(a, b)
#     return square(sum)

# print(add_and_square(2, 3))

# def categorize_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20:
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Old"

# print(categorize_age(22))

# def add(a, b):
#     return a+b

# pair = (3,5)
# result = add(*pair)
# print(result)

# def divide(a, b):
#     number1 = a // b
#     remainder = a % b
#     return number1, remainder

# result, result2 = divide(10, 3)
# print(result)



