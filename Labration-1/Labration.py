from scanner import _scan, _scan_os

def ip_adress():
    while True:
        try:
            ip_file = input("\nFile(e.g 'file.txt'): ")
            if ip_file == 'x':
                break
        
            with open(ip_file, 'r') as file:
                print(f"'{ip_file}' Successfully opened!\n")
                ip_list.clear()
                line = file.readline()
                while line:
                    ip_list.append(line)
                    line = file.readline()
                break
                
        except FileNotFoundError:
            print(f"Could not find file '{ip_file}'")
            print("Enter 'x' to exit. ")

def save_file():
    while True:
        print('--------------------------')
        print("****Save Options****")
        print("1: Save to Existing File")
        print("2: Save to New File")
        print("3: Back")
        
        try:
            new_or_old = int(input("Choose an option between 1-3: "))

            if new_or_old > 0:
                if new_or_old == 1:
                    while True:
                        try:
                            existing_file_name = input("File(e.g 'file.txt'): ")
                            if existing_file_name == 'x':
                                break

                            with open(existing_file_name) as file:
                                print(f"'{existing_file_name}' Set as savefile!\n")
                                save_settings.clear()
                                save_settings.append(existing_file_name)
                                break

                        except FileNotFoundError:
                            print(f"Could not find file '{existing_file_name}'")
                            print("Enter 'x' to exit. ")
                    break
                elif new_or_old == 2:
                    while True:
                        try:
                            new_file_name = input("File(e.g 'file.txt'): ")
                            if new_file_name == 'x':
                                break

                            with open(new_file_name, 'x') as file:
                                print(f"\n'{new_file_name}' Set as savefile!\n")
                                save_settings.clear()
                                save_settings.append(new_file_name)
                                break

                        except FileExistsError:
                            print(f"File already exists '{new_file_name}'")
                            print("Enter 'x' to exit. ")
                    break
                elif new_or_old == 3:
                    break
                else:
                    print("\n*Invalid input*")
                    print("***************")
        except ValueError:
            print("\nMust be a number between 1-3") 

def settings():

    while True:
        print('--------------------------')
        print("****Settings Menu**** ")
        print("1: Load IP-Addresses") 
        print("2: Choose a Savefile")
        print("3: Show Settings") 
        print("4: Back")

        try:
            choice = int(input("Choose an option between 1-4: "))
            if choice > 0:
                if choice == 1:
                    ip_adress()
                elif choice == 2:
                    save_file()
                elif choice == 3:
                    print(f"IP-Addresses: {ip_list}")
                    print(f"Savefile: {save_settings}")
                elif choice == 4:
                    break
                else:
                    print("\n*Invalid input*")
                    print("***************")
        except ValueError:
            print("\nMust be a number between 1-4")   


def scan():
    
    while True:
        print('--------------------------')
        print("****Scan Menu****")
        print("1: Host status, port(1-1000), port-state & service")
        print("2: OS Scan")
        print("3: Insert own flag(s)")
        print("4: Back")

        try:
            choice = int(input("Choose an option between 1-4: "))
            if 0 < choice:
                if choice == 1:
                    option = ""
                    _scan(ip_list, save_settings, option)
                elif choice == 2:
                    _scan_os(ip_list, save_settings)
                elif choice == 3:
                    print("This will still only print out Host status, ports(state and service)")
                    option = input("Enter flag(s) to run(e.g -sV -Pn -p): ")
                    _scan(ip_list, save_settings, option)
                elif choice == 4:
                    break
                else:
                    print("\n*Invalid input*")
        except ValueError:
            print("\nMust be a number between 1-4")

def main():

    global ip_list
    global save_settings
    ip_list = []
    save_settings = []

    while True:
        print('--------------------------')
        print("****Nmap Menu****")
        print("1: Settings")
        print("2: Scan")
        print("3: Exit")

        try:
            choice = int(input("Choose an option between 1-3: "))
            if 0 < choice:
                if choice == 1:
                    settings()
                elif choice == 2:
                    scan()
                elif choice == 3:
                    print("Exiting")
                    break
                elif choice == 4:
                    print(ip_list, save_settings)
                else:
                    print("\n*Invalid input*")
        except ValueError:
            print("\nMust be a number between 1-3")   


if __name__ == "__main__":
    main()

