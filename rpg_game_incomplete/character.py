# basic rpg character system

class Character:
        
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 0
        self.attack = 0
        self.mana = None
        self.style = ""


    def show_status(self):
        size = len(self.name) + 4
        print("=" * size)
        print(f"{self.name}".center(size))
        print("=" * size)
        print(f"Style: {self.style}\nLevel: {self.level}\nHealth: {self.health}")

        if self.mana:
            print(f"Mana: {self.mana}")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100
        self.health = 80
        self.style = "Mage"


    def fireball(self):
        self.mana -= 25
        



class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.style = "Warrior"


class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.style = "Archer"


class Healer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 50
        self.health = 90
        self.style = "Healer"


class Beast(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 130
        self.style = "Beast"