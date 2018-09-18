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
        self.start_health = int(health)
        self.health = int(health)
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
        if self.health > 0:
            self.health -= damage_amt
            if self.health <= 0:
                self.deaths += 1
                return 1
            return 0

    def add_kill(self, num_kills):
        self.kills += num_kills


class Ability:
    name = ''
    attack_strength = 0

    def __init__(self, name, attack_strength):
        self.name = name
        lowest = int(attack_strength) // 2
        self.attack_strength = random.randint(lowest, int(attack_strength))

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
        self.defense = int(defense)

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
                    deaths += 1
        return deaths

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def check_heroes(self):
        for hero in self.heroes:
            if hero.health > 0:
                return True
        return False

    def stats(self):
        for hero in self.heroes:
            print("{}: \n       kills: {}\n       deaths: {}".format(
                hero.name, hero.kills, hero.deaths))

    def update_kills(self, kills):
        for hero in self.heroes:
            hero.add_kill(kills)


class Arena:
    team_one = None
    team_two = None

    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team(self, team):
        team_name = user_input('Enter name for team {}: '.format(team))
        team = Team(team_name)
        add_heroes = True
        hero_count = 1
        
        while add_heroes:
            print('enter \'quit\' to cancel')
            name = user_input('Enter name for hero {}: '.format(hero_count))
            health = user_input('Enter health for {}: default(100) '.format(name))

            hero = Hero(name, health)

            add_ab = user_input('Add abilities to {}? (y/n) '.format(name))
            if add_ab.lower() == 'y':
                add_abilities = True
            elif add_ab.lower() == 'n':
                add_abilities = False
            while add_abilities:
                ab_name = user_input('Enter name for ability: ')
                ab_power = user_input('Enter power for {}: '.format(ab_name))
                ability = Ability(ab_name, ab_power)
                hero.add_ability(ability)
                add_another = user_input('Add another ability to {}? (y/n) '.format(name))
                if add_another.lower() == 'n':
                    add_abilities = False

            add_ar = user_input('Add armor to {}? (y/n) '.format(name))
            if add_ar.lower() == 'y':
                add_armor = True
            elif add_ar.lower() == 'n':
                add_armor = False
            while add_armor:
                ar_name = user_input('Enter name for armor: ')
                ar_power = user_input('Enter power defense for {}: '.format(ar_name))
                armor = Armor(ar_name, ar_power)
                hero.add_armor(armor)
                add_another = user_input('Add more armor to {}? (y/n) '.format(name))
                if add_another.lower() == 'n':
                    add_armor = False

            # add_wp = user_input('Add weapons to {}? (y/n) '.format(name))
            # if add_wp.lower() == 'y':
            #     add_weapons = True
            # elif add_wp.lower == 'n':
            #     add_weapons = False
            # while add_weapons:
            #     wp_name = user_input('Enter name for weapon: ')
            #     wp_power = user_input('Enter power for {}: '.format(wp_name))
            #     weapon = Weapon(wp_name, wp_power)
            #     hero.add_weapon(weapon)
            #     add_another = user_input('Add another weapon to {}? (y/n) '.format(name))
            #     if add_another.lower == 'n':
            #         add_weapons = False


            team.add_hero(hero)
            hero_count += 1
            print('Created {} as a hero for team {}.'.format(name, team_name))
            add_another = user_input('Add another hero to team {}? (y/n) '.format(team_name))
            if add_another.lower() == 'n':
                    add_heroes = False

        return team

    def build_team_one(self):
        name = user_input('Enter name for team 1: ')
        self.team_one = Team(name)
        add_heroes = True
        hero_count = 1
        while add_heroes:
            print('enter \'quit\' to cancel')
            name = user_input('Enter name for hero {}: '.format(hero_count))
            if name == 'quit':
                add_heroes = False
                break
            health = user_input(
                'Enter health for {}: default(100) '.format(name))
            if health == 'quit':
                add_heroes = False
                break

            if health and int(health) > 0:
                self.team_one.add_hero(Hero(name, health))
            else:
                self.team_one.add_hero(Hero(name))

            hero_count += 1

            print('Added {} to team 1.'.format(name))

    def build_team_two(self):
        name = user_input('Enter name for team 2: ')
        self.team_two = Team(name)
        add_heroes = True
        hero_count = 1
        while add_heroes:
            print('enter \'quit\' to cancel')
            name = user_input('Enter name for hero {}: '.format(hero_count))
            if name == 'quit':
                add_heroes = False
                break
            health = user_input(
                'Enter health for {}: default(100) '.format(name))
            if health == 'quit':
                add_heroes = False
                break

            if health and int(health) > 0:
                self.team_two.add_hero(Hero(name, health))
            else:
                self.team_two.add_hero(Hero(name))

            hero_count += 1

            print('Added {} to team 2.'.format(name))

    def team_battle(self):
        teams_alive = True
        while teams_alive:
            team_one_alive = self.team_one.check_heroes()
            team_two_alive = self.team_two.check_heroes()
            
            if team_one_alive and team_two_alive:
                self.team_one.attack(self.team_two)
                self.team_two.attack(self.team_one)
            else:
                teams_alive = False

        self.show_stats()

    def show_stats(self):
        print('{} statistics:\n\n'.format(self.team_one.name))
        self.team_one.stats()

        print('__________________________________________________')

        print('{} statistics:\n\n'.format(self.team_two.name))
        self.team_two.stats()


def user_input(prompt):
    try:
        user_input = input(prompt)
        return user_input

    except EOFError:
        return ''


if __name__ == "__main__":
    arena = Arena()
    arena.team_one = arena.build_team(1)
    arena.team_two = arena.build_team(2)
    arena.team_battle()
