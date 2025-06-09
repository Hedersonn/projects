# ====================================
#     System Login / Register Tool
# ====================================

# imports / values
from functions import interface, system_login
import requests
import pygame

path = "C:/Users/pajeh/OneDrive/Documentos/estudos/projects/login_v1_complete/users/users.txt"
path_music = "C:/Users/pajeh/OneDrive/Documentos/estudos/projects/login_v1_complete/music.mp3"

# central

option = interface.menu("Log in", "Sign in", "Quit")

# verify options

match option:
    
    case 1: # log in
        confirm_menu_login = system_login.logIn(path)

        if confirm_menu_login:
            system_login.loginChoice(path_music)
        else:
            interface.end_system()

    case 2: # sign in
        system_login.signIn(path)

    case 3: # exit
        interface.end_system()






                        
                

    




