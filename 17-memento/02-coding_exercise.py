# Memento Coding Exercise
# A TokenMachine  is in charge of keeping tokens. Each Token  is a reference type with a single numerical value.
# The machine supports adding tokens and, when it does, it returns a memento representing the state of that system at that given time.
# You are asked to fill in the gaps and implement the Memento design pattern for this scenario.
# Pay close attention to the situation where a token is fed in as a reference and its value is
# subsequently changed on that reference - you still need to return the correct system snapshot!

class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    def __init__(self, tokens: list[Token]):
        super().__init__()
        for t in tokens:
            self.append(t.value)


class TokenMachine:
    def __init__(self):
        self.tokens = []
        self.changes = [Memento(self.tokens)]
        self.current = 0

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token: Token):
        self.tokens.append(token)
        m = Memento(self.tokens)
        self.changes.append(m)
        self.current += 1
        return m

    def revert(self, memento):
        # todo
        if memento:
            self.tokens = [Token(val) for val in memento]
            self.changes.append(memento)
            self.current = len(self.changes) - 1
    
    def __str__(self) -> str:
        return ' '.join([str(t.value) for t in self.tokens]) 


if __name__ == "__main__":
    tm = TokenMachine()

    m1 = tm.add_token_value(10)
    print(tm)

    m2 = tm.add_token_value(20)
    print(tm)

    m3 = tm.add_token_value(30)
    print(tm)

    tm.revert(m2)
    print(tm)

    print("test")