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

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        return (("*" * self.width) + "\n") * self.height

    def set_width(self, width):
        self.width = abs(width)

    def set_height(self, height):
        self.height = abs(height)