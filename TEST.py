

path = "C:/Users/pajeh/OneDrive/Documentos/estudos/MyProjects/projects/login/users/users.txt"

users = []
with open(path, "rt") as file:
    for user in file:
        verify_users = user.replace("\n", "").split(":")
        user_dict = {
            "username": verify_users[0],
            "password": verify_users[1]
        }
        users.append(user_dict)
        

print(users)