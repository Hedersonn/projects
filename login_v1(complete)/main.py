# ====================================
#     System Login / Register Tool
# ====================================

# imports / values
from functions import interface, system_login
import requests
import pygame

path = "C:/Users/pajeh/OneDrive/Documentos/estudos/projects/login_v1/users/users.txt"
path_music = "C:/Users/pajeh/OneDrive/Documentos/estudos/projects/login_v1/music.mp3"

# central

option = interface.menu("Log in", "Sign in", "Quit")

# verify options

match option:
    case 1: # log in
        system_login.logIn(path)
        choice = interface.menu("Coins", "Music", "Quit", menu=False)
        match choice:
            case 1:
                try:
                    interface.lines("COINS")
                    info = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD")
                    info = info.json()
                    real = info["BRLUSD"]["bid"]
                    euro = info["EURUSD"]["bid"]
                    btc = info["BTCUSD"]["bid"]
                    print(f"R$ {real}\n€ {euro}\nBTC {btc}\n")
                except:
                    print("There was an error loading the information.")
            case 2:
                try:
                    interface.lines("MUSIC")
                    pygame.mixer.init()
                    pygame.mixer_music.load(path_music)
                    pygame.mixer.music.play()
                    input("Press any key to stop the music\n")
                    pygame.mixer.quit()
                except:
                    print("There was an error loading the music.")
            case 3:
                interface.end_system()
                
    case 2: # sign in
        system_login.signIn(path)
    case 3: # exit
        interface.end_system()






                        
                

    




