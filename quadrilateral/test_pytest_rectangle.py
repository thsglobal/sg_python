from quadrilateral.rectangle import Rectangle


# Tests for innate methods
def test_rectangle_repr():
    assert repr(Rectangle(4,5)) == "Rectangle(width=4, height=5)"


def test_rectangle_str():
    assert str(Rectangle(4,5)) == "(4,5)"


# Tests for the area method
def test_rectangle_area():
    assert Rectangle(4, 5).get_area() == 20


def test_rectangle_negative_area():
    assert Rectangle(-4, 5).get_area() == 20
    assert Rectangle(4, -5).get_area() == 20
    assert Rectangle(-4, -5).get_area() == 20


# Tests for the perimeter method
def test_rectangle_perimeter():
    assert Rectangle(4, 5).get_perimeter() == 18


def test_rectangle_negative_perimeter():
    assert Rectangle(-4, 5).get_perimeter() == 18
    assert Rectangle(4, -5).get_perimeter() == 18
    assert Rectangle(-4, -5).get_perimeter() == 18


def test_rectangle_set_width():
    rect = Rectangle(4,5)
    assert rect.get_perimeter() == 18
    rect.set_width(3)
    assert rect.get_perimeter() == 16


def test_rectangle_set_height():
    rect = Rectangle(4,5)
    assert rect.get_perimeter() == 18
    rect.set_height(4)
    assert rect.get_perimeter() == 16


def test_rectangle_get_picture():
    assert Rectangle(90,90).get_picture() == "Too big for picture"
    assert Rectangle(3,3).get_picture() == "***\n***\n***\n"