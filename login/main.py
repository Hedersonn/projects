# ====================================
#     System Login / Register Tool
#     Access your music securely 🎵
# ====================================

# imports / values
import functions

users = []

path = "C:/Users/pajeh/OneDrive/Documentos/estudos/MyProjects/projects/login/users/users.txt"


# verify file exist
try:
    with open(path, "rt") as file:
        file.read()
except:
    with open(path, "wt+") as file:
        file.read()

# transform file in dict

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
    print("error transform")

# central

confirm = True
option = functions.menu("Log in", "Sign in", "Quit")

# verify options

match option:
    case 1: # log in
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
        functions.lines(texto="SIGN IN")




                            
                    

        
    



