import os
from collections import deque
import curses

from debugger import debug


def sample(a, b):
    q = deque()
    for i in range(b):
        q.append(a)
    return q


def sample1(a, b):
    arr = []
    i = 0
    for i in range(b):
        arr.append(i)
        i += 1
    return arr


if __name__ == "__main__":
    os.system('color')
    curses.start_color()
    curses.echo()
    # note: only one function can work at at time (i.e. overlap can occur)
    debug(sample, (2, 5))
    # debug(sample1, (3, 5))
