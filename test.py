from rpg_game_incomplete.functions.character import Mage, Archer, Beast, Healer, Warrior, Character
from random import randint


player1 = Mage("Mage")
player2 = Beast("Beast")
player3 = Archer("Archer")
player4 = Healer("Healer")
player5 = Warrior("Warrior")

players = [player1, player2, player3, player4, player5]

current_index = randint(0, len(players) - 1)
cont = 0

while True:
    current_index = (current_index + 1) % len(players)
    attacker = players[current_index]
    print(f"\n===> It`s {attacker.name}`s turn!")

    for index, player in enumerate(players):

        if index != current_index:
            print(f"{index + 1} - {player.name}")


    choice = int(input("Who will you attack?"))

    if choice > 0 and choice < len(players) + 1:
        print(f"{players[choice - 1].name}")

    else:
        print("Type a valid value.")