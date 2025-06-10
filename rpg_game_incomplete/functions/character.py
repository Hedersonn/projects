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

    def fireball(self, target):
        self.mana -= 20
        target.health -= 35

    def frost_lance(self, target):
        pass
    
    def arcane_shield(self, target):
        pass

    def runic_teleport(self, target):
        pass

    def foresight(self, target):
        pass
            

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)

        self.health = 150
        self.style = "Warrior"

    def devastating_strike(self, target):
        pass

    def battle_fury(self, target):
        pass
    
    def iron_wall(self, target):
        pass
    
    def defensive_stance(self, target):
        pass
    
    def war_cry(self, target):
        pass


class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        
        self.health = 100
        self.style = "Archer"

    def piercing_shot(self, target):
        pass

    def arrow_rain(self, target):
        pass

    def silent_step(self, target):
        pass

    def natural_camouflage(self, target):
        pass

    def eagle_eye(self, target):
        pass


class Healer(Character):
    def __init__(self, name):
        super().__init__(name)

        self.mana = 50
        self.health = 90
        self.style = "Healer"

    def punishing_light(self, target):
        pass

    def aura_of_peace(self, target):
        pass

    def circle_of_protection(self, target):
        pass

    def celestial_heal(self):
        pass

    def revitalize(self):
        pass


class Beast(Character):
    def __init__(self, name):
        super().__init__(name)

        self.health = 130
        self.style = "Beast"

    def savage_charge(self, target):
        pass

    def vorpal_claws(self, target):
        pass

    def thick_hide(self):
        pass

    def animal_instinct(self):
        pass

    def pack_howl(self):
        pass