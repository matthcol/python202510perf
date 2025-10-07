import pytest
from point import Point

@pytest.fixture
def point_1():
    return Point(x=3.5, y=2.25)

@pytest.fixture
def point_2():
    return Point(x=7.5, y=5.25)


def test_eq_when_same(point_1):
    assert point_1 == point_1

def test_eq_when_copy(point_1):
    point_1_copy = Point(x=point_1.x, y=point_1.y)
    assert point_1 == point_1_copy
    assert point_1_copy == point_1

def test_eq_when_different_coords(point_1, point_2):
    assert not point_1 == point_2

def test_eq_when_other_not_a_point(point_1):
    assert not point_1 == 'a text'
    assert not 'a text' == point_1

#TODO: faire tous les tests duaux pour !=
def test_ne():
    pass

def test_another():
    pass