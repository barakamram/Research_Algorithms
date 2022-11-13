
from q1 import *
import pytest


def test_1():
    assert safe_call(f, x=5, y=7.0, z=3) == 15.0


def test_2():
    assert safe_call(f, x=5, y=15.0, z=-10) == 10.0


def test_3():
    assert safe_call(f, x=5, y=2.0, z="abc") == f'7.0abc'


def test_4():
    assert safe_call(f, x=3, y=-1.3, z=-1.7) == 0.0


def test_5():
    with pytest.raises(Exception) as error:
        safe_call(f, x=5, y="abc", z=3)
    assert str(error.value) == "Wrong Type: expected: <class 'float'> but got: <class 'str'>"


def test_6():
    with pytest.raises(Exception) as error:
        safe_call(f, x=2, y=-1, z=-1)
    assert str(error.value) == "Wrong Type: expected: <class 'float'> but got: <class 'int'>"


def test_7():
    with pytest.raises(Exception) as error:
        safe_call(f, x=3.0, y=0.0, z="abb")
    assert str(error.value) == "Wrong Type: expected: <class 'int'> but got: <class 'float'>"


def test_8():
    assert safe_call(f, x=3, y=-1.3, z=-3) == -1.3


def test_9():
    assert safe_call(f2, x="a", y="bb", z="ccc") == "abbccc"


def test_10():
    assert safe_call(f2, x="ba", y="r", z="ak") == "barak"


if __name__ == "__main__":
    pass
