class Creature:
    def __init__(self, game, attack, defense):
        self.game = game
        self._attack = attack
        self._defense = defense

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, var):
        self._defense = var

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, var):
        self._attack = var


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def defense(self):
        if self not in self.game.creatures:
            return self._defense 
        nr_other_goblins = 0
        for c in self.game.creatures:
            if c is self:
                continue
            if issubclass(type(c), Goblin):
                nr_other_goblins += 1
        self._defense += nr_other_goblins
        return self._defense

    @property
    def attack(self):
        if self not in self.game.creatures:
            return self._attack 
        nr_other_goblin_kings = 0
        for c in self.game.creatures:
            if c is self:
                continue
            if issubclass(type(c), GoblinKing):
                nr_other_goblin_kings += 1
        self._attack += nr_other_goblin_kings
        return self._attack
             

class GoblinKing(Goblin):
    def __init__(self, game):
        super.__init__(game, 3, 3)


class Game:
    def __init__(self):
        self.creatures = []
    

if __name__ == "__main__":
    game = Game()
    goblin = Goblin(game)
    game.creatures.append(goblin)

    assert (goblin.attack == 1)
    assert (goblin.defense == 1)