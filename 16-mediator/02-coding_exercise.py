# Mediator Coding Exercise
# Our system has any number of instances of Participant  classes. Each Participant has a value integer attribute, initially zero.
# A participant can say()  a particular value, which is broadcast to all other participants.
# At this point in time, every other participant is obliged to increase their value  by the value being broadcast.
# Example:
# Two participants start with values 0 and 0 respectively
# Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3
# Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.join(self)

    def say(self, value):
        # todo
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self) -> None:
        self._participants: list[Participant] = []

    def join(self, participant: Participant):
        self._participants.append(participant)
    
    def broadcast(self, source: Participant, value: int):
        for p in self._participants:
            if p is not source:
                p.value += value


if __name__ == "__main__":
    med = Mediator()

    p1 = Participant(med)
    p2 = Participant(med)
    # p3 = Participant(med)

    p1.say(3)
    print(f"P1 = {p1.value}; P2 = {p2.value}")

    p2.say(2)
    print(f"P1 = {p1.value}; P2 = {p2.value}")

