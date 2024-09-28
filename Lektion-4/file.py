import os
## Skapa ett verktyg som kan läsa, skriva och söka i textfiler

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.readlines()
            print("**********")
            for line in content:
                print(line.strip())
            print("")
    else:
        print(f"File doesnt exist: {filename}")

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print(f"File was created: {filename} \n")
    else:
        print(f"File already exists: {filename} \n")


def append_file(filename, text):
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            file.write('\n' + text)
        print(f"Text added to file {filename} \n")
    else:
        print(f"File was not found {filename} \n")
            
def search_file(filename, text):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            found = False
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if text in line:
                    print(f"The word {text} was found on line {i}")
                    found = True
        if found == False:
            print("No matching line found")    
    else:
        print(f"File not found: {filename}")





# Main program

while True:
    print("**********")
    print("Menu:")
    print("1. Read file")
    print("2. Create file")
    print("3. Append text to file")
    print("4. Search for text in file")
    print("5. Exit")

    choice = input("Chose an option (1-4)")

    if choice == '1':
        filename = input('Enter the filename: ')
        read_file(filename)
    elif choice == '2':
        filename = input('Enter the filename: ')
        create_file(filename)
    elif choice == '3':
        filename = input('Enter the filename: ')
        text = input("\nEnter text to append: ")
        append_file(filename, text)
    elif choice == '4':
        filename = input('Enter the filename: ')
        text = input("\nEnter searchword ")
        search_file(filename, text)
    elif choice == '5':
        print("Exiting program")
        break
    else:
        print("Invalid choice")
