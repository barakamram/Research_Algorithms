import doctest


class List(list):
    def __getitem__(self, k):
        """
        >>> lst = List([[['a','b','c',33],[4,5,[3, 1, 2], 6, 66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
        >>> lst[0,1,2,1] == 1
        True
        >>> lst[0,1,4] == 66
        True
        >>> lst[0,0,2] == 'c'
        True
        >>> lst[0,1] == [4,5,[3, 1, 2], 6,66]
        True
        """
        if not isinstance(k, int):
            r = list(self)
        else:
            return list(self)[k]
        for key in k:
            r = r[key]
        return r


if __name__ == "__main__":
    list1 = List([[['a', 'b', 'c', 33], [4, 5, [3, 1, 2], 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]],
                    [[], [[13, 14, 15, 155], [16, 17, 18, 188]]]])

    print(list1[0, 1] == [4, 5, [3, 1, 2], 6, 66])
    print(list1[0, 0, 0] == 'a')
    print(list1[0, 1, 2] == [3, 1, 2])
    print(list1[2, 1] == [[13, 14, 15, 155], [16, 17, 18, 188]])
    print(list1[2, 1, 1, 3] == 188)
    print(list1[2, 0] == [])
    doctest.testmod()