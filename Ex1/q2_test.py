from q2 import *


def test_1():
    trail = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    assert breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function) == trail


def test_2():
    trail = [(3, 5), (2, 5), (1, 5), (0, 5), (-1, 5), (-2, 5), (-2, 4), (-2, 3), (-2, 2)]
    assert breadth_first_search(start=(3, 5), end=(-2, 2), neighbor_function=four_neighbor_function) == trail


def test_3():
    trail = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10)]
    assert breadth_first_search(start=(0, 0), end=(2, 10), neighbor_function=four_neighbor_function) == trail


def test_4():
    trail = [(-3, -3), (-2, -3), (-1, -3), (0, -3), (1, -3), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (1, 3)]
    assert breadth_first_search(start=(-3, -3), end=(1, 3), neighbor_function=four_neighbor_function) == trail


def test_5():
    trail = [(0, 0), (-1, 0), (-2, 0), (-2, 1), (-2, 2)]
    assert breadth_first_search(start=(0, 0), end=(-2, 2), neighbor_function=four_neighbor_function) == trail


def test_6():
    trail = [(20, -10), (19, -10), (18, -10), (17, -10), (16, -10), (15, -10), (14, -10),
           (13, -10), (12, -10), (11, -10), (10, -10), (9, -10), (8, -10), (7, -10), (6, -10),
           (5, -10), (4, -10), (3, -10), (2, -10), (1, -10), (0, -10), (-1, -10), (-2, -10),
           (-3, -10), (-4, -10), (-5, -10), (-6, -10), (-7, -10), (-8, -10), (-9, -10),
           (-10, -10), (-10, -9), (-10, -8), (-10, -7), (-10, -6), (-10, -5), (-10, -4),
           (-10, -3), (-10, -2), (-10, -1), (-10, 0), (-10, 1), (-10, 2), (-10, 3), (-10, 4),
           (-10, 5), (-10, 6), (-10, 7), (-10, 8), (-10, 9), (-10, 10), (-10, 11), (-10, 12),
           (-10, 13), (-10, 14), (-10, 15), (-10, 16), (-10, 17), (-10, 18), (-10, 19),
           (-10, 20)]
    assert breadth_first_search(start=(20, -10), end=(-10, 20), neighbor_function=four_neighbor_function) == trail


if __name__ == "__main__":
    pass
