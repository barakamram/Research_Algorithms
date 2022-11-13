from q3 import *
import pytest


def test_1():
    expected = {"a": 5, "b": [1, 2, 3, 4], "c": 6}
    to_sort = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    assert print_sorted(to_sort) == expected


def test_2():
    expected = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}
    to_sort = {"e": 1, "d": 2, "c": 3, "b": 4, "a": 5}
    assert print_sorted(to_sort) == expected


def test_3():
    expected = {'a': 432, 'b': ['apple', 'avocado', 'banana', 'chita', ['a', 'd', 'e', 'f', [1, 2, 3, 5]]], 'c': [7, 8, 9, 10]}
    to_sort = {"c": [10, 9, 8, 7], "b": ["banana", "avocado", ["d", "f", "a", [2, 5, 3, 1], "e"], "chita", "apple"], "a": 432}
    assert print_sorted(to_sort) == expected


def test_4():
    expected = {'a': 121, 'b': [1, 5, 6, 7], 'd': [1, 4, 5, [1, 2, 3]], 'e': ['barak', 'beer', 'dictionary', 'list', 'zebra']}
    to_sort = {"e": {"barak", "zebra", "beer", "dictionary", "list"}, "b": [5, 6, 7, 1], "a": 121, "d": [5, 4, [3, 1, 2], 1]}
    assert print_sorted(to_sort) == expected


def test_5():
    expected = {'a': 5, 'b': [1, 2, 3, 4], 'c': 6, 'd': 'acbd', 'e': ['barak', 'beer', 'dictionary', 'list', 'zebra'], 'f': {'a': ("(5, 'b', 4, 3)", '2', "['a', 1]"), 'b': ['apple', 'avocado', 'banana', 'chita', ['a', 'd', 'e', 'f', [1, 2, 3, 5]]], 'c': 6, 'd': 'acbd', 'e': 5}, 'g': ('1', '3', '5', 'a', 'c')}
    to_sort = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "g": (1, 5, "c", 3, "a"),
            "f": { "e": 5, "c": 6, "b": ["banana", "avocado", ["d", "f", "a", [2, 5, 3, 1], "e"], "chita", "apple"],
                 "a": (["a", 1], 2, (5, "b", 4, 3)), "d": "acbd"},
           "e": {"barak", "zebra", "beer", "dictionary", "list"}, "d": "acbd"}
    assert print_sorted(to_sort) == expected


if __name__ == "__main__":
    pass
