
def sort_lst(l, struct):  # this is for list in list in list etc..
    lst = []
    for i in l:
        if isinstance(i, list):
            temp = i
            l.remove(i)
            lst = sort_lst(temp, list)
    l = sorted(l)
    if len(lst) > 0:
        l.append(lst)
    return struct(l)


def print_sorted(x):
    to_sort = {}
    for element in x:
        if isinstance(x[element], int):
            to_sort[element] = x[element]

        elif isinstance(x[element], str):
            to_sort[element] = x[element]

        elif isinstance(x[element], list):
            to_sort[element] = sort_lst(x[element], list)

        elif isinstance(x[element], set):
            to_sort[element] = sorted(x[element])
            # to_sort[element] = sort_lst(x[element], list)

        elif isinstance(x[element], tuple):
            # to_sort[element] = sorted(x[element])
            to_sort[element] = tuple(sorted(tuple(map(str, x[element]))))

        elif isinstance(x[element], dict):
            to_sort[element] = print_sorted(x[element])

    sorted_list = {}
    for key in sorted(to_sort):
        sorted_list[key] = to_sort[key]
    return sorted_list


if __name__ == "__main__":
    x1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print('sorted x1 ----->', print_sorted(x1))
    # {"a":5, "b":[1,2,3,4], "c":6}

    x2 = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "g": (1, 5, "c", 3, "a"),
     "f": {"e": 5, "c": 6, "b": ["banana", "avocado", ["d", "f", "a", [2, 5, 3, 1], "e"], "chita", "apple"],
           "a": (["a", 1], 2, (5, "b", 4, 3)), "d": "acbd"},
     "e": {"barak", "zebra", "beer", "dictionary", "list"}, "d": "acbd"}
    print('sorted x2 ----->', print_sorted(x2))
    # {'a': 5, 'b': [1, 2, 3, 4], 'c': 6, 'd': 'acbd', 'e': ['barak', 'beer', 'dictionary', 'list', 'zebra'],
    # 'f': {'a': ("(5, 'b', 4, 3)", '2', "['a', 1]"), 'b': ['apple', 'avocado', 'banana', 'chita', ['a', 'd', 'e', 'f', [1, 2, 3, 5]]],
    # 'c': 6, 'd': 'acbd', 'e': 5}, 'g': ('1', '3', '5', 'a', 'c')}

