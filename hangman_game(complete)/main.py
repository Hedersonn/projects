# hangman game

# imports
import random

# word list

word_list = ["apple", "stone", "knife", "notebook", "coffee", "sky"]
word_aleatory = random.choice(word_list)

# principal values

analist = []
chance = 5
win = False
check_accuracy = len(word_aleatory)
start = True

for letter in word_aleatory:
    analist.append("-")

for letter in analist:
    print(letter, end="")

# start game

while start:
    print(f"\nChances: {chance}")
    letter_choice_player = str(input("\nType a letter: "))
    confirm = False
    
    for index, letter in enumerate(word_aleatory):

        if letter_choice_player == letter and analist[index] == "-":
            analist[index] = letter_choice_player
            check_accuracy -= 1
            confirm = True

    for letter in analist:
        print(letter, end="")

    if not confirm:
        chance -= 1
    if check_accuracy == 0 or chance == 0:
        start = False
    print()

if chance == 0:
    print("Unfortunately you didn't make it.")
else:
    print("Congratulations, you did it!")
    
print(f"Word: {word_aleatory}")
