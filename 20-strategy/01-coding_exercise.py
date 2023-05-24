import math
from abc import ABC, abstractmethod


class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c):
        return


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        e1 = pow(b, 2)
        e2 = (4 * a * c)
        return (e1 - e2)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        e1 = pow(b, 2)
        e2 = (4 * a * c)
        discrim = (e1 - e2)
        if discrim < 0:
            return float('nan')
        return discrim


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        real_1 = (-b / (2 * a))
        real_2 = real_1

        imag = 0
        discrim = self.strategy.calculate_discriminant(a, b, c)
        if not math.isnan(discrim):
            if discrim >= 0:
                discrim = math.sqrt(discrim) / (2 * a)
                real_1 += discrim
                real_2 -= discrim
            else:
                discrim *= -1
                imag = math.sqrt(discrim) / (2 * a)
        else:
            return (float('nan'), float('nan'))
        
        return (complex(real_1, imag), complex(real_2, -imag))
    

if __name__ == "__main__":
    qes = QuadraticEquationSolver(RealDiscriminantStrategy())
    res = qes.solve(1, 4, 5)
    print(res)
    print("Test")