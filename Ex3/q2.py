import doctest

memory_dict = {}


def lastcall(func):
    """
    >>> f_pow(2)
    4
    >>> f_pow(2)
    'I already told you that the answer is 4!'
    >>> f_pow(10)
    100
    >>> f_pow(2)
    'I already told you that the answer is 4!'
    >>> f_pow(10)
    'I already told you that the answer is 100!'
    """
    def wrap(*args, **kwargs):
        if func not in memory_dict.keys():
            memory_dict[func] = dict()
        if args not in memory_dict[func]:
            memory_dict[func][args] = func(*args, **kwargs)  # there is the only line the function runs.
            return memory_dict[func][args]
        return f"I already told you that the answer is {memory_dict[func][args]}!"
    return wrap


@lastcall
def f_pow(x: int):
    return x ** 2


@lastcall
def f_add(x: float, y: float):  # 2 params
    return x + y


def st(x: str):  # if x starts with lower-case change it to an upper-case
    name = x
    if ord(x[0]) > 90:  # check if its lower-case form
        name = chr(ord(x[0]) - 32) + x[1:]
    return f_str(name)


@lastcall
def f_str(x: str):
    return "Welcome " + x + "! nice to see you"


@lastcall
def f_avg(*args):  # avg of args
    s = 0
    for v in args:
        s += v
    return s/len(args)


if __name__ == '__main__':
    doctest.testmod()
    print('f_pow(3) ---> ', f_pow(3))
    print('f_pow(-3) ---> ', f_pow(-3))
    print('f_pow(3) again ---> ', f_pow(3))
    print('f_pow(3) again X2 ---> ', f_pow(3))
    print('\t')

    print('f_add(5.5, 4.5) ---> ', f_add(5.5, 4.5))
    print('f_add(10.1, 9.9) ---> ', f_add(10.1, 9.9))
    print('f_add(4.5, 5.5) ---> ', f_add(4.5, 5.5))
    print('f_add(5.5, 4.5) again ---> ', f_add(5.5, 4.5))
    print('\t')

    print("f_str('barak') ---> ", st('barak'))
    print("f_str('Barak') again ---> ", st('Barak'))
    print("f_str('tal') ---> ", st('tal'))
    print("f_str('Tal') again ---> ", st('Tal'))
    print("f_str('barak amram') ---> ", st('barak amram'))
    print("f_str('Barak amram') ---> ", st('barak amram'))
    print('\t')

    print('f_avg(5,4,3) ---> ', f_avg(5, 4, 3))
    print('f_avg(3,4,5) ---> ', f_avg(3, 4, 5))
    print('f_avg(3,4,6,7) ---> ', f_avg(3, 4, 6, 7))
    print('f_avg(3,4,6,7,15,32,52) ---> ', f_avg(3, 4, 6, 7, 15, 32, 52))
    print('f_avg(5,4,3) again ---> ', f_avg(5, 4, 3))
    print('f_avg(3,4,6,7,15,32,52) again ---> ', f_avg(3, 4, 6, 7, 15, 32, 52))
