# Template Method Coding Exercise
# Imagine a typical collectible card game which has cards representing creatures. Each creature has two values: Attack and Health.
# Creatures can fight each other, dealing their Attack damage, thereby reducing their opponent's health.
# The class CardGame implements the logic for two creatures fighting one another. However, the exact mechanics of how damage is dealt is different:
# TemporaryCardDamage : In some games (e.g., Magic: the Gathering), unless the creature has been killed,
# its health returns to the original value at the end of combat.
# PermanentCardDamage : In other games (e.g., Hearthstone), health damage persists.
# You are asked to implement classes TemporaryCardDamageGame  and PermanentCardDamageGame  that would allow us to simulate combat between creatures.
# Some examples:
# With temporary damage, creatures 1/2 and 1/3 can never kill one another. With permanent damage, second creature will win after 2 rounds of combat.
# With either temporary or permanent damage, two 2/2 creatures kill one another.

from abc import ABC, abstractmethod


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        self.hit(self.creatures[c1_index], self.creatures[c2_index])
        both_alive = self.creatures[c1_index].health > 0 and self.creatures[c2_index].health > 0
        both_dead = self.creatures[c1_index].health <= 0 and self.creatures[c2_index].health <= 0
        if (both_alive or both_dead):
            return -1
        else:
            if self.creatures[c1_index].health <= 0:
                return c2_index
            elif self.creatures[c2_index].health <= 0:
                return c1_index
    
    @abstractmethod
    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        def_init_health = defender.health
        att_init_health = attacker.health

        defender.health -= attacker.attack
        attacker.health -= defender.attack
        if defender.health > 0:
            defender.health = def_init_health
        if attacker.health > 0:
            attacker.health = att_init_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        attacker.health -= defender.attack