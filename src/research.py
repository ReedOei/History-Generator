from Tkinter import *

import random

class Weapon:
    def __init__(self, name, range, material_multiplier, attack, defense, attack_skill_multiplier, defense_skill_multiplier, reload_time=0, ammunition=0):
        self.name = name

        self.range = range

        self.material_multiplier = material_multiplier

        self.attack = attack
        self.defense = defense

        self.attack_skill_multiplier = attack_skill_multiplier
        self.defense_skill_multiplier = defense_skill_multiplier

        self.reload_time = reload_time
        self.ammunition = ammunition

    def get_attack(self, material):
        effective_attack = self.attack

        if material != None and self.material_multiplier > 0:
            effective_attack = int(effective_attack * self.material_multiplier * material.effect_strength)

        return random.randint(0, effective_attack)

    def get_defense(self, material):
        effective_defense = self.defense

        if material != None and self.material_multiplier > 0:
            effective_defense = int(effective_defense * self.material_multiplier * material.effect_strength)

        return random.randint(0, effective_defense)

    def copy(self):
        return Weapon(self.name, self.range, self.material_multiplier, self.attack, self.defense, self.attack_skill_multiplier, self.defense_skill_multiplier, self.reload_time, self.ammunition)

    def __call__(self):
        return self.copy()

    def __repr__(self):
        return '{} (x{}): {} ({}), {} ({})'.format(self.name, self.material_multiplier, self.attack, self.attack_skill_multiplier, self.defense, self.defense_skill_multiplier)

class Armor:
    def __init__(self, name, material_multiplier, defense, defense_skill_multiplier):
        self.name = name

        self.material_multiplier = material_multiplier

        self.defense = defense
        self.defense_skill_multiplier = defense_skill_multiplier

    def get_defense(self, material):
        effective_defense = self.defense

        if material != None and self.material_multiplier > 0:
            effective_defense = int(effective_defense * self.material_multiplier * material.effect_strength)

        return random.randint(0, effective_defense)

    def copy(self):
        return Armor(self.name, self.material_multiplier, self.defense, self.defense_skill_multiplier)

    def __call__(self):
        return self.copy()

    def __repr__(self):
        return '{} (x{}): {} ({})'.format(self.name, self.material_multiplier, self.defense, self.defense_skill_multiplier)

#------------------------------
# WEAPON AND ARMOR DEFINITIONS
#------------------------------

#Short
unarmed = Weapon('Unarmed', 5, 0, 1, 1, 1, 1)
dagger = Weapon('Dagger', 5, 1.5, 2, 2, 1.1, 1)
rondel = Weapon('Rondel', 5, 1.6, 3, 1, 1.5, 1)
dirk = Weapon('Dirk', 5, 1.6, 3, 1, 1.5, 1)
kopis = Weapon('Kopis', 6, 1.8, 6, 1, 2, 1)
shortsword = Weapon('Shortsword', 7, 1.8, 5, 2, 2, 1.1)
club = Weapon('Club', 7, 0, 5, 2, 1, 1)
hammer = Weapon('Hammer', 7, 1.3, 6, 1, 1.5, 0.8)
mace = Weapon('Mace', 7, 1.5, 6, 1, 1.8, 1.0)
axe = Weapon('Axe', 7, 1.8, 8, 2, 2.5, 0.8)
morning_star = Weapon('Morning Star', 7, 1.5, 8, 0, 2, 0.2)

#Medium
sword = Weapon('Sword', 10, 2, 6, 3, 2, 1.1)
bastard_sword = Weapon('Bastard Sword', 12, 2.3, 7, 2, 2, 1.5)
claymore = Weapon('Claymore', 15, 2.5, 10, 1, 2.5, 0.5)
bill = Weapon('Bill', 12, 1.5, 6, 4, 1.5, 1.5)
flail = Weapon('Flail', 12, 1.2, 6, 0, 2, 0.5)
falx = Weapon('Falx', 14, 1.8, 8, 1, 2, 0.8)

#Long
staff = Weapon('Staff', 15, 0, 3, 3, 2, 2)
spear = Weapon('Spear', 20, 1.0, 4, 4, 1.5, 1.5)
pike = Weapon('Pike', 25, 1.0, 5, 5, 1.5, 1.5)
sarissa = Weapon('Sarissa', 35, 1.0, 7, 3, 2, 2)

all_melee_weapons = [unarmed, kopis, mace, falx, club, hammer, dagger, rondel, dirk, shortsword, sword, bastard_sword, claymore, spear, staff, bill, pike, sarissa, axe, flail, morning_star]
weapon_list = [sword, mace, falx, shortsword, bastard_sword, claymore, spear, staff, pike, sarissa, axe, flail, morning_star, bill]

sidearm_list = [dagger, club, mace, kopis, hammer, rondel, dirk, staff, shortsword, axe, spear]
basic_weapon_list = [club, mace, hammer, staff, shortsword, axe, spear]

stones = Weapon('Stones', 90, 0, 1, 1, 1, 1, reload_time=20, ammunition=6)
sling = Weapon('Sling', 250, 0, 3, 1, 1.8, 1, reload_time=50, ammunition=25)
javelin = Weapon('Javelin', 125, 0.5, 6, 2, 1.5, 1, reload_time=20, ammunition=3)
atlatl = Weapon('Atlatl', 175, 0.5, 8, 1, 2.0, 1, reload_time=70, ammunition=8)
shortbow = Weapon('Shortbow', 300, 0.5, 4, 1, 2, 1, reload_time=70, ammunition=15)
bow = Weapon('Bow', 350, 0.5, 5, 1, 2, 1, reload_time=80, ammunition=15)
longbow = Weapon('Longbow', 400, 0.5, 6, 1, 2.5, 1, reload_time=90, ammunition=15)
crossbow = Weapon('Crossbow', 450, 1.5, 10, 1, 1, 1, reload_time=300, ammunition=15)
sling_staff = Weapon('Sling Staff', 300, 0, 5, 2, 2, 1, reload_time=60, ammunition=20)

all_ranged_weapons = [stones, atlatl, sling, shortbow, longbow, javelin, bow, crossbow, sling_staff]
ranged_weapon_list = [sling, atlatl, javelin, shortbow, longbow, bow, crossbow, sling_staff]

basic_ranged_list = [stones, sling, javelin, shortbow, bow]

cloth_armor = Armor('Cloth Armor', 0, 2, 0.5)
padded_armor = Armor('Padded Armor', 0, 3, 0.5)
leather_armor = Armor('Leather Armor', 0, 4, 0.4)
wood_armor = Armor('Wood Armor', 0, 5, 0.3)
chainmail = Armor('Chaimail', 1, 8, 0.25)
plate = Armor('Plate', 2, 12, 0.15)

all_armor_list = [cloth_armor, padded_armor, leather_armor, wood_armor, chainmail, plate]

armor_list = [wood_armor, chainmail, plate]
basic_armor_list = [cloth_armor, leather_armor, wood_armor, padded_armor]

#------------------------------

def base_tech_tree():
    return Tech('Agriculture', 'agriculture', 0, 1.0,
                [
                    Tech('Stone Working', 'material', 100, 1.1,
                    [
                        Tech('Copper', 'material', 400, 1.5,
                        [
                            Tech('Bronze', 'material', 800, 2.0,
                            [
                                Tech('Iron', 'material', 1600, 2.5,
                                [
                                    Tech('Steel', 'material', 3200, 3.0, [])
                                ])
                            ])
                        ])
                    ]),
                    Tech('Improved Housing', 'housing', 200, 1.5, []),
                    Tech('Improved Mining', 'mining', 400, 2.0, []),
                    Tech('Improved Agriculture', 'agriculture', 150, 1.1, [])
                ])

class Tech:
    def __init__(self, name, category, research_points, effect_strength, next_techs):
        self.name = name
        self.category = category

        self.current_research_points = 0
        self.research_points = research_points

        self.effect_strength = effect_strength

        self.next_techs = next_techs

    def is_unlocked(self):
        return self.current_research_points >= self.research_points

    def get_tech(self, tech_name):
        if self.name == tech_name and self.is_unlocked():
            return self
        else:
            for next_tech in self.next_techs:
                res = next_tech.get_tech(tech_name)
                if res != None:
                    return res

            return None
    def has_tech(self, tech_name):
        if self.name == tech_name:
            return self.is_unlocked()
        else:
            for next_tech in self.next_techs:
                if has_tech(next_tech, tech_name):
                    return True

            return False

    def get_best_in_category(self, category_name):
        for i in self.next_techs:
            if i.category == category_name and i.is_unlocked():
                return i.get_best_in_category(category_name)

        if self.category == category_name:
            return self

        return None

    def get_available_research(self):
        if self.is_unlocked():
            result = []
            for next_tech in self.next_techs:
                result.extend(next_tech.get_available_research())
            return result
        else:
            return [self]

    def do_research(self, research_amount):
        if not self.is_unlocked():
            self.current_research_points += research_amount
