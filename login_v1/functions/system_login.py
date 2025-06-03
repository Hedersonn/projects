def dictUsers(path):
    users = []
    try:
        with open(path, "rt") as file:
            for user in file:
                verify_users = str(user).replace("\n", "").split(":")
                user_dict = {
                    "username": verify_users[0],
                    "password": verify_users[1]
                }
                users.append(user_dict)
        return users
    except:
        with open(path, "wt+") as file:
            file.read()


def logIn(path):
    try:
        dict_users = dictUsers(path)
        from functions import interface
        confirm = True
        interface.lines("LOG IN")

        while confirm:
            username = str(input("Username: ")).strip()
            password = str(input("Password: ")).strip()

            for user in dict_users:
                if user["username"] == username and user["password"] == password:
                    print("PASS")
                    confirm = False
                    break
            else:
                print("User or password incorrect")
                try_again = str(input("Try again? Y | N: "))[0]

                if try_again in "Nn":
                    confirm = False
    except:
        print("There was an error logging in user.")


def signIn(path):
    try:
        dict_users = dictUsers(path)
        from functions import interface
        confirm = True
        interface.lines("SIGN IN")
        
        while confirm:
            username = str(input("Create username: ")).strip()
            password = str(input("Create password: ")).strip()
            confirm_password = str(input("Confirm password: ")).strip()

            for user in dict_users:

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
    except:
        print("There was an error registering the user.")
