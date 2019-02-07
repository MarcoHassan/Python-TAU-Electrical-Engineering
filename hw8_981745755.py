##########################
## Homework Nr. 8       ##
## ID Number: 981745755 ##
## Name: Marco Hassan   ##
##########################

# Import numpy to check for real numbers
import numpy as np


# Implement all methods of class Creature
class Creature:
    def __init__(self, race, life, weapon_name, weapon_power):
        if type(race) != str or type(weapon_name) != str:
            raise AttributeError(f'race, {race}, and weapon name, {weapon_name}, must be strings.')
        elif np.isreal(life) == False:
            raise AttributeError(f'life, {life}, must be a real number.')
        else:
            if weapon_power > 0 and type(weapon_power) == int:
                self.race = race
                self.life = life
                self.weapon_name = weapon_name
                self.weapon_power = weapon_power
            else:
                raise AttributeError(f'weapon_power, {weapon_power}, must be a positive integer.')

    def hit(self, other):
        if self.is_alive() != True or other.is_alive() != True:
            return

        else:
            self.life -= 5

            hit_power = self.weapon_power + (self.life)/4
            other.absorb(hit_power)

    def absorb(self, hit_power):
        self.life -= hit_power

    def is_alive(self):
        if self.life > 5:
            return True
        else:
            return False

    def get_life(self):
        return self.life

    def get_race(self):
        return self.race


# Implement class GoodCreature
class GoodCreature(Creature):
    def __init__(self, race, life, weapon_name, weapon_power):
        Creature.__init__(self, race, life, weapon_name, weapon_power)

    def get_race(self):
        return "good " + Creature.get_race(self)

    def hit(self, other):
        Creature.hit(self, other)
        other.absorb((self.life)/4)


# Implement class BadCreature
class BadCreature(Creature):
    def __init__(self, race, life, weapon_name, weapon_power, shield_power):
        Creature.__init__(self, race, life, weapon_name, weapon_power)

        if shield_power < 0 or type(shield_power) != int:
            raise ValueError(f'shield power [{shield_power}] must be a positive integer.')
        else:
            self.shield_power = shield_power

    def absorb(self, hit_power):
        Creature.absorb(self, hit_power)
        self.life += self.shield_power


class Battle:
    def __init__(self, good_army, bad_army):

        def loop_integrity(army, type_army, invalid_Creature):
            for i in range(0, len(army)):
                if type(army[i]) is invalid_Creature:
                    raise AttributeError(f'The army is a {type_army} and cannot contain {invalid_Creature.__name__}')
            if army == good_army:
                self.good_army = army
            else:
                self.bad_army = army

        loop_integrity(good_army, "good_army", BadCreature)
        loop_integrity(bad_army, "bad_army", GoodCreature)

    def dual_fight(self, good_index, bad_index):
        i = 0
        while self.good_army[good_index].get_life() > 5 and self.bad_army[bad_index].get_life() > 5:
            i += 1
            self.bad_army[bad_index].hit(self.good_army[good_index])
            if self.good_army[good_index].get_life() < 5:
                break
            self.good_army[good_index].hit(self.bad_army[bad_index])
        return i

# Implement class TotalBattle


class TotalBattle(Battle):
    def __init__(self, good_army, bad_army):
        Battle.__init__(self, good_army, bad_army)

    def dual_fight(self, good_index, bad_index):
        return Battle.dual_fight(self, good_index, bad_index)

    def fight(self):
        i = 0
        while len(self.good_army) > 0 and len(self.bad_army) > 0:
            i += int(self.dual_fight(0, 0))
            if self.good_army[0].life < 5:
                self.good_army.remove(self.good_army[0])
            if self.bad_army[0].life < 5:
                self.bad_army.remove(self.bad_army[0])
        if len(self.bad_army) > 0:
            return "Evil won " + str(i)
        elif len(self.good_army) > 0:
            return "Self.Good guys won " + str(i)
        else:
            return "Draw " + str(i)
