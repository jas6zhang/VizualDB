from collections import deque
import curses

from vector import Vector
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue

SCREEN = curses.initscr()

def visualization_factory(ds):
    if hasattr(ds, 'visualize'):
        ds.visualize()


def check_type(ds):
    if isinstance(ds, list):
        return Vector(ds)
    elif isinstance(ds, Node):
        return LinkedList(ds)
    elif isinstance(ds, deque):
        return DoubleEndedQueue(SCREEN, ds)
    return
