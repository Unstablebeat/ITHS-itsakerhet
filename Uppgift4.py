import os

save_file = open("ip-ping.txt", 'w')
with open("ip-adresser" , 'r') as file:
    ip_address = file.readline()
    while ip_address:
        result = os.popen(f"ping -n 1 {ip_address}").read()
        print(result)
        save_file.write(result + "\n" + "***********" + "\n")
        ip_address = file.readline()
save_file.close()