#System Login

# read file
def readFile(path):
    from colorama import Fore, Style, init
    init(autoreset=True)
    try:
        with open(path, "r") as file:
            file.read() # verify_file
    except:
        with open(path, "wt+") as file:
            file.read() # create_file
    else:
        try:
            with open(path, "r") as users:
                file = users.read()
                return file
        except:
            return Fore.RED + Style.BRIGHT + "Error! Please, verify you file."
        

# append users
def register(path, printUser, printPass):

    from colorama import Fore, init, Style
    init(autoreset=True)

    while True:   
        try:
            users = []
            username = str(input(printUser))

            with open(path, "r") as usernames:

                for user in usernames:
                    user_existing = user.strip().split(":") [0]
                    users.append(user_existing)

                if username in users:
                    print("Error! User already exists")
                else:
                    with open(path, "a") as user:

                        password = str(input(printPass))
                        return user.write(f"{username}:{password}\n")
        except:
            return Fore.RED + Style.BRIGHT + "Error! Please, verify you file."
    


# scanning users

# def scanningFile(function):
#     usernames = function
#     users = []
#     for user in usernames:
#         user.split(":")
#         user.replace("\n","")
#         users.append(user[0])
#         # for username in users:
#     print(users)
            
            
    


            

