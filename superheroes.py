import random


class Hero:
    name = ''
    abilities = list()
    armors = list()
    start_health = 0
    health = 0
    deaths = 0
    kills = 0

    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        attack_power = 0

        if self.health <= 0:
            return 0

        for ability in self.abilities:
            attack_power += ability.attack()
        return attack_power

    def defend(self):
        defense_power = 0

        if self.health <= 0:
            return 0

        for armor in self.armors:
            defense_power += armor.defend()
        return defense_power

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            return 1
        return 0

    def add_kill(self, num_kills):
        self.kills += num_kills


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
        return random.randint(0, self.attack_strength)


class Armor:
    name = ''
    defense = 0

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


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

    def attack(self, other_team):
        attack_power = 0
        for hero in self.heroes:
            attack_power += hero.attack()
        kills = other_team.defend(attack_power)
        self.update_kills(kills)

    def defend(self, damage_amt):
        defense_power = 0
        for hero in self.heroes:
            defense_power += hero.defend()
        damage = damage_amt - defense_power
        self.deal_damage(damage)
        kills = 0
        if damage > 0:
            damage_per_hero = damage // len(self.heroes)
            for hero in self.heroes:
                dead = hero.take_damage(damage_per_hero)
                if dead == 1:
                    kills += 1
        return kills

    def deal_damage(self, damage):
        deaths = 0
        if damage > 0:
            damage_per_hero = damage // len(self.heroes)
            for hero in self.heroes:
                dead = hero.take_damage(damage_per_hero)
                if dead == 1:
                    hero.deaths += 1
                    deaths += 1
        return deaths

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            print("{}: \n       kills: {}\n       deaths: {}".format(hero.name, hero.kills, hero.deaths))

    def update_kills(self, kills):
        for hero in self.heroes:
            hero.add_kill(kills)


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
