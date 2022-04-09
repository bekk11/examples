import turtle


class Rectangle:

    def __init__(self, sides, width, height):
        self.sides = sides
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.sides):
            turtle.forward(self.width)
            turtle.right(self.height)
        turtle.done()


rect = Rectangle(4, 200, 90)
rect.draw()