import random

class Hero:
    name = ''
    abilities = list()

    def __init__(self, name):
        self.name = name
        self.abilities = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        attack_power = 0
        for ability in self.abilities:
            attack_power += ability.attack()
        return attack_power

class Ability:
    name = ''
    attack_strength = 0

    def __init__(self, name, attack_strength):
        self.name = name
        lowest = attack_strength // 2
        self.attack_strength = random.randint(lowest, attack_strength)

    def attack(self):
        return self.attack_strength

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        rand_val = random.randint(0, self.attack_strength)
        return rand_val

class Team:
    name = ''
    heroes = list()

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(index)
                return
            index += 1
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())