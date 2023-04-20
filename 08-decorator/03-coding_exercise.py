from unittest import TestCase


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        # todo
        return f'A circle of radius {self.radius}'


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        # todo
        return f"A square with side {self.side}"


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        # todo
        # note that a Square doesn't have resize()
        if hasattr(self.shape, "resize"):
            self.shape.resize(factor)
        else:
            raise NotImplementedError

    def __str__(self):
        # todo
        return f"{self.shape} has the color {self.color}"


class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual('A circle of radius 5 has the color red', str(circle))
        circle.resize(2)
        self.assertEqual('A circle of radius 10 has the color red', str(circle))

    def test_square(self):
        square = ColoredShape(Square(2), 'red')
        square.resize(2)

if __name__ == "__main__":
    ev = Evaluate()
    ev.test_circle()
    ev.test_square()