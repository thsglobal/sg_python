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
