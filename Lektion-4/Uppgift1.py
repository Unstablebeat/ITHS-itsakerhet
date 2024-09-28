def isnumber(number):
    if number.isdigit():
        return True
    else:
        return False

def _multiplication_table(multiply, max):
    start = 0
    while start <= max:
        value = multiply * start
        print(f"{multiply} times {start} = {value}")
        start += 1

number_to_multiply = input("What number do you want to multiply?: ")
number_max = input("How high you want the table?: ")

if isnumber(number_to_multiply) & isnumber(number_max) == True:
    print("")
    _multiplication_table(int(number_to_multiply), int(number_max))
else:
    print("Thats not a number")
