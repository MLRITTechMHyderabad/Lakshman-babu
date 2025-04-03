class Character:
    def __init__(self,name,health, attack_power, defence, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
        self.speed = speed
    
    def attack(self, target):
        damage = max(1, self.attack_power - target.defence)
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} Deals {damage} damage")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. remaining health {self.health} ")

    def is_Alive(self):
        if self.health > 0:
            return True
        else:
            return False
        

class Warrior(Character):  #Here we're inherite the parent/super class(Character), child class(Warrior)
    def __init__(self, health, attack_power, defence, speed, rage):
        super().__init__(health, attack_power, defence, speed)
        self.rage = rage
    
    def Berserk_Mode(self):
        if self.health < 0.3:
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")
        

class Mage(Character):
    def __init__(self, health, attack_power, defence, speed, mana):
        super().__init__(health, attack_power, defence, speed)
        self.mana = mana

    def Fireball(self):
        pass

class Archer(Character):
    def __init__(self, health, attack_power, defence, speed, critical_chance):
        super().__init__(health, attack_power, defence, speed)
        self.critical_chance = critical_chance
    
    def Precision_Shot(self):
        pass