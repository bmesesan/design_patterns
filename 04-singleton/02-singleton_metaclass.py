class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {}

    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         cls._instances[cls] = super(Singleton, cls)\
    #             .__call__(*args, **kwargs)
    #     return cls._instances[cls]

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self)\
                .__call__(*args, **kwargs)
        return self._instances[self]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
