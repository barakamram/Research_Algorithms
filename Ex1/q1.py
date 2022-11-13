
def f(x: int, y: float, z):
    if isinstance(z, str):
        return f'{x+y}{z}'
    return x+y+z


def f2(x: str, y, z: str):
    return x+y+z


def safe_call(f, **kwargs):
    annotations = f.__annotations__
    for k in annotations.keys():
        if type(kwargs[k]) is not annotations[k]:  # throw exception
            raise Exception(f"Wrong Type: expected: {annotations[k]} but got: {type(kwargs[k])}")
    return f(**kwargs)


if __name__ == "__main__":
    print(safe_call(f, x=5, y=7.0, z=3))  # returns 15.0
    print(safe_call(f, x=3, y=7.0, z=0))  # returns 10.0
    print(safe_call(f, x=2, y=-3.0, z=1.5))  # returns 0.5
    print(safe_call(f, x=2, y=-3.0, z="abc"))  # returns -1.0abc
    print(safe_call(f2, x="a", y="bb", z="ccc"))  # returns abbccc
    print(safe_call(f, x=5, y="abc", z=3))  # raises an exception

