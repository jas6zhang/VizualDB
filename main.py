import os

from debugger import debug


def sample(a, b):
    arr = []
    for i in range(b):
        arr.append(a)
    return arr


if __name__ == "__main__":
    os.system('color')
    debug(sample, (2, 5))
