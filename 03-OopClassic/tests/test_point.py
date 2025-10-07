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


def test_add_with_scalar(point_1):
    point = point_1 + 2.5
    assert point.x == 6.0
    assert point.y == 4.75

def test_add_with_tuple(point_1):
    point = point_1 + (2.5, 2.25)
    assert point.x == 6.0
    assert point.y == 4.5

def test_add_with_point(point_1):
    point = point_1 + Point(2.5, 2.25)
    assert point.x == 6.0
    assert point.y == 4.5

@pytest.mark.parametrize(
        "rhs",
        [
            "a text",
            False,
            None,
            (12.3, 12.5, 13.4),
            (12.5, 'a'),
            ('a', 12.5),
        ],
        ids=[
            "str",
            "bool",
            "None",
            "tuple of length 3",
            "tuple[float, str]",
            "tuple[str, float]",
        ]
)
def test_add_with_unsupported_type(point_1, rhs):
    with pytest.raises(TypeError):
        # hook: __enter__
        _ = point_1 + rhs
    # hook __exit__ : check if exception TypeError happens


def test_radd_with_scalar(point_1):
    point = 2.5 + point_1
    assert point.x == 6.0
    assert point.y == 4.75

def test_radd_with_tuple(point_1):
    point = (2.5, 2.25) + point_1
    assert point.x == 6.0
    assert point.y == 4.5

@pytest.mark.parametrize(
        "rhs",
        [
            "a text",
            False,
            None,
            (12.3, 12.5, 13.4),
            (12.5, 'a'),
            ('a', 12.5),
        ],
        ids=[
            "str",
            "bool",
            "None",
            "tuple of length 3",
            "tuple[float, str]",
            "tuple[str, float]",
        ]
)
def test_radd_with_unsupported_type(point_1, rhs):
    with pytest.raises(TypeError):
        # hook: __enter__
        _ = rhs + point_1 
    # hook __exit__ : check if exception TypeError happens


def test_iadd_with_scalar(point_1):
    point_1 += 2.5
    assert point_1.x == 6.0
    assert point_1.y == 4.75

def test_iadd_with_tuple(point_1):
    point_1 += (2.5, 2.25)
    assert point_1.x == 6.0
    assert point_1.y == 4.5

def test_iadd_with_point(point_1):
    point_1 += Point(2.5, 2.25)
    assert point_1.x == 6.0
    assert point_1.y == 4.5

@pytest.mark.parametrize(
        "rhs",
        [
            "a text",
            False,
            None,
            (12.3, 12.5, 13.4),
            (12.5, 'a'),
            ('a', 12.5),
        ],
        ids=[
            "str",
            "bool",
            "None",
            "tuple of length 3",
            "tuple[float, str]",
            "tuple[str, float]",
        ]
)
def test_iadd_with_unsupported_type(point_1, rhs):
    with pytest.raises(TypeError):
        # hook: __enter__
        point_1 += rhs
    # hook __exit__ : check if exception TypeError happens
