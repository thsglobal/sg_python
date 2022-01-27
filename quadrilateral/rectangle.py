class Rectangle:
    def __init__(self, width, height):
        self.height = abs(height)
        self.width = abs(width)

    def __str__(self):
        return f"({self.width},{self.height})"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)