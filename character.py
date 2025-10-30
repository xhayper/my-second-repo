import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        attack_point = (random.randint(30, 90) / 100) * self.attack_power
        other.hp -= attack_point
        print(f"{self.name} attacks {other.name} for {attack_point} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
