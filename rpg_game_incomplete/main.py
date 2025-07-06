from functions.character import Mage, Warrior, Archer, Healer, Beast
from functions import utilities
from random import randint

p1 = Mage("Player 1")
p2 = Healer("Player 2")
p3 = Archer("Player 3")

players = [p1, p2, p3]
current_index = randint(0, len(players) - 1)
chosen_player = players[current_index].name
print(chosen_player, "started.")

while True:
    while True:
        utilities.title(f"{players[current_index].name} chooses")

        for index, player in enumerate(players):
            if index != current_index:
                print(f"{index + 1} - {player.name}")

        attack = int(input("Who will you attack? ")) - 1

        if attack == current_index:
            print("Error, enter a number other than yours.")
        # elif attack > len(players) or attack <= 0:
        #     print("Number not exist.")
        else:
            break

    choice = utilities.menu("Attack", "Defense", "Support")
    match choice:
        case 1:
            print(players[current_index].skills[attack])

            
    