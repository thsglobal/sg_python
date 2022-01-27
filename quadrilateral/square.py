from quadrilateral.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def __str__(self):
        return f"({self.width})"

    def __repr__(self):
        return f"Square(width={self.width})"

    def get_number_enclosing(self, other):
        return (int((self.get_area() / other.get_area()) ** 0.5)) ** 2

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height