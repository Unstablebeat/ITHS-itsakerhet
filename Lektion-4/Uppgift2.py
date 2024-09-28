def addition(num1, num2):
    result = num1 + num2
    print(f"The value of {num1} + {num2} is: {result}!")

def subtraction(num1, num2):
    result = num1 - num2
    print(f"The value of {num1} - {num2} is: {result}!")

def multiplikation(num1, num2):
    result = num1 * num2
    print(f"The value of {num1} * {num2} is: {result}!")

def division(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Sorry you can't devide by 0")
    else:
        result = num1 / num2
        print(f"The value of {num1} / {num2} is: {result}!")


while True:
    print("Menu")
    print("Choose a function between 1-5")
    print("Option 1: Addition")
    print("Option 2: Subtraction")
    print("Option 3: Multiplication")
    print("Option 4: Division")
    print("Option 5: Exit")

    choice = input("Option: ")

    if choice.isdigit() and int(choice) < 5 and int(choice) > 0:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        if choice == "1":
            addition(num1, num2)
        elif choice == "2":
            subtraction(num1, num2)
        elif choice == "3":
            multiplikation(num1, num2)
        elif choice == "4":
            division(num1, num2)
    elif choice == "5":
        print("Exiting")
        break
    else:
        print("\n***************")
        print("*Invalid input*")
        print("***************\n")

    print("*************\n")



