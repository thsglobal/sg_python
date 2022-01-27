from quadrilateral.square import Square


# Tests for innate methods
def test_square_repr():
    assert repr(Square(5)) == "Square(width=5)"


def test_square_str():
    assert str(Square(5)) == "(5)"


def test_square_area():
    assert Square(5).get_area() == 25


def test_square_perimeter():
    assert Square(5).get_perimeter() == 20


def test_square_negative_area():
    assert Square(-5).get_area() == 25


def test_square_negative_perimeter():
    assert Square(-5).get_perimeter() == 20


def test_square_number_enclosing():
    assert Square(10).get_number_enclosing(Square(1)) == 100


def test_square_negative_number_enclosing():
    assert Square(-10).get_number_enclosing(Square(1)) == 100
    assert Square(10).get_number_enclosing(Square(-1)) == 100
    assert Square(-10).get_number_enclosing(Square(-1)) == 100
