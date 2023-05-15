# Imagine a game where one or more rats can attack a player.
# Each individual rat has an initial attack value of 1.
# However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.
# Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method,
# please implement the Game and Rat classes so that, at any point in the game, the Attack value of a rat is always consistent.

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        # todo
        self.rat_joined_event = Event()
        self.rat_leaves_event = Event()
        self.nr_rats = 0
        self.rat_joined_event.append(increase_nr_rats)
        self.rat_leaves_event.append(decrease_nr_rats)


class Rat(object):
    def __init__(self, game: Game):
        self.game = game
        self._attack = 1
        self.join_event_called = False

        self.game.rat_joined_event(self.game)
        self.join_event_called = True
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_leaves_event(self.game)

    @property
    def attack(self):
        self._attack = self.game.nr_rats
        return self._attack


def increase_nr_rats(game):
    game.nr_rats += 1


def decrease_nr_rats(game):
    game.nr_rats -= 1


if __name__ == "__main__":
    game = Game()
 
    rat = Rat(game)
    assert (1 == rat.attack)
 
    rat2 = Rat(game)
    assert (2 == rat.attack)
    assert (2 == rat2.attack)
 
    with Rat(game) as rat3:
        assert (3 == rat.attack)
        assert (3 == rat2.attack)
        assert (3 == rat3.attack)
 
    assert (2 == rat.attack)
    assert (2 == rat2.attack)
    
