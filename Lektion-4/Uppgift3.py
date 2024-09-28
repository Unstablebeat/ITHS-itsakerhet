
def _show_items():
    print("The items in the list are: ")
    print(shoppinglist)

def _add_items():
    item_list = input("What would you like to add?\n(seperate by space for multiple) ").split()

    for item in item_list:
        if item in shoppinglist:
            print(f"{item} is already in the shoppinglist\n")
        else:
            print(f"{item} was added to the shoppinglist")
            shoppinglist.append(item)

def _remove_items():
    item = input("What would you like to remove? ")
    if item in shoppinglist:
        shoppinglist.remove(item)
        print(f"\n{item} was removed from the shoppinglist")
    else:
        print(f"\n{item} Does not exist in the shoppinglist")

def _save_items():
    name = input("What would you like to name the file? ").strip(".txt")
    with open(f"{name}.txt", 'w') as file:
        for item in shoppinglist:
            file.write(item + "\n")
    print(f"Saved as {name}.txt")

shoppinglist = []

while True:
    print("Menu: ")
    print("Choose a option between 1-5")
    print("Option 1: Show Item(s)")
    print("Option 2: Add Item(s)")
    print("Option 3: Remove Item(s)")
    print("Option 4: Save Item(s)")
    print("Option 5: Exit")

    choice = input("What would you like to do? ")

    if choice.isdigit() and int(choice) < 5 and int(choice) > 0:
        
        if choice == "1":
            _show_items()
        elif choice == "2":
            _add_items()
        elif choice == "3":
            _remove_items()
        elif choice == "4":
            _save_items()
    elif choice == "5":
        print("Exiting")
        break
    else:
        print("\n***************")
        print("*Invalid input*")
        print("***************")

    print("*************\n")
