class Shape:
    def __init__(self):
        self.area = None

    def area(self):
        self.area = 0
        return self.area


class Square(Shape):
    def __init__ (self, length):
        self.length = length
        self.area = 4 * self.length
        print(self.area)


c = Square(4)
