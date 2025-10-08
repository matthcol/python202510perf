import pytest
import model


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected_distance, margin",
    [
        (3.5, 15.25, 6.5, 11.25, 5.0, 0.0),
        (3.5E300, 15.25E300, 6.5E300, 11.25E300, 5.0E300, 1E-15),
        (3.5E-300, 15.25E-300, 6.5E-300, 11.25E-300, 5.0E-300, 0.0),
    ],
    ids=[
        "normal scale",
        "big scale",
        "small scale",
    ]
)
def test_distance(x1, y1, x2, y2, expected_distance, margin):
    p1 = model.Point(x=x1, y=y1)
    p2 = model.Point(x=x2, y=y2)
    actual_distance = p1.distance(p2)
    assert actual_distance == pytest.approx(expected_distance, rel=margin)