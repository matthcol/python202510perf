import numpy as np
import pytest

import geoapp.model as model


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected_distance, margin",
    [
        (3.5, 15.25, 6.5, 11.25, 5.0, 0.0),
        (3.5e300, 15.25e300, 6.5e300, 11.25e300, 5.0e300, 1e-15),
        (3.5e-300, 15.25e-300, 6.5e-300, 11.25e-300, 5.0e-300, 0.0),
    ],
    ids=[
        "normal scale",
        "big scale",
        "small scale",
    ],
)
def test_distance(x1, y1, x2, y2, expected_distance, margin):
    p1 = model.Point(x=np.float64(x1), y=np.float64(y1))
    p2 = model.Point(x=np.float64(x2), y=np.float64(y2))
    actual_distance = p1.distance(p2)
    assert actual_distance == pytest.approx(expected_distance, rel=margin)
