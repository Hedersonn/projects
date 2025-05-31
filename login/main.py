# ====================================
#     System Login / Register Tool
#     Access your music securely 🎵
# ====================================

# imports / values
import functions

users = []

path = "C:/Users/pajeh/OneDrive/Documentos/estudos/projects/login/users/users.txt"


# verify file exist / transform file in dict

try:
    with open(path, "rt") as file:
        for user in file:
            verify_users = str(user).replace("\n", "").split(":")
            user_dict = {
                "username": verify_users[0],
                "password": verify_users[1]
            }
            users.append(user_dict)
except:
    with open(path, "wt+") as file:
        file.read()

# central

option = functions.menu("Log in", "Sign in", "Quit")

# verify options

match option:
    case 1: # log in
        confirm = True
        functions.lines(texto="LOG IN")

        while confirm:
            username = str(input("Username: ")).strip()
            password = str(input("Password: ")).strip()

            for user in users:
                if user["username"] == username and user["password"] == password:
                    print("PASS")
                    confirm = False
                    break
            else:
                print("User or password incorrect")
                try_again = str(input("Try again? Y | N: "))[0]

                if try_again in "Nn":
                    confirm = False
    case 2:
        confirm = True
        functions.lines(texto="SIGN IN")
        
        while confirm:
            username = str(input("Create username: ")).strip()
            password = str(input("Create password: ")).strip()
            confirm_password = str(input("Confirm password: ")).strip()

            for user in users:

                if user["username"] == username:
                    print("username already exists")
                    try_again = str(input("Try again? Y | N: "))[0] .strip()
                    if try_again in "Nn":
                        confirm = False
                    break
                        
            else:
                if password == confirm_password:
                    with open(path, "a") as user_password:
                        user_password.write(f"{username}:{password}\n")
                        print("Created successfully")
                        confirm = False
                else:
                    print("Wrong password")
                try_again = str(input("Try again? Y | N: "))[0] .strip()
                if try_again in "Nn":
                    confirm = False
    case 3:
        print("Thank for testing")
                        






                            
                    

        
    



