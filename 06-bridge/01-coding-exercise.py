from abc import ABC


class Renderer(ABC):
    def render_as_triangle(self):
        pass

    def render_as_square(self):
        pass
    

class VectorRenderer(Renderer):
    def render_as_triangle(self):
        return "Drawing Triangle as lines"

    def render_as_square(self):
        return "Drawing Square as lines"


class RasterRenderer(Renderer):
    def render_as_triangle(self):
        return "Drawing Triangle as pixels"

    def render_as_square(self):
        return "Drawing Square as pixels."


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer


class Triangle(Shape):
    def __init__(self, renderer: Renderer): 
        super().__init__(renderer)
    
    def __str__(self) -> str:
        return self.renderer.render_as_triangle()


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
    
    def __str__(self) -> str:
        return self.renderer.render_as_square()