from src.monitor import check_threshold


def test_below_threshold():
    assert check_threshold(84.9) == "OK"


def test_at_threshold():
    assert check_threshold(85.0) == "OK"


def test_above_threshold():
    assert check_threshold(85.1) == "WARNING"