# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234",
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]
###---------------------###
###-Your-code-goes-here-###
###---------------------###

#Gör om dictionary till items sedan till en lista med dessa
credentials_items = user_credentials.items()
credentials_items_list = list(credentials_items)

with open("password_results", 'w') as file:
    for user in range(len(credentials_items_list)): 
        for password in range(len(password_list)): 
            if credentials_items_list[user][1] == password_list[password]:
                result_success = f"{credentials_items_list[user][0]}: {password_list[password]} -> Success"
                file.write(result_success + "\n")
                print(result_success)
            else:
                result_failed = f"{credentials_items_list[user][0]}: {password_list[password]} -> failed"
                file.write(result_failed + "\n")
                print(result_failed)
        file.write("\n")
        print("")

