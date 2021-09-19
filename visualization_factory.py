
from vector import Vector
from hash_map import HashMap
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue

SCREEN = curses.initscr()


def visualization_factory(ds):
    if hasattr(ds, 'visualize'):
        ds.visualize()


def check_type(ds):

    if isinstance(ds, list):
        return Vector(ds)
    elif isinstance(ds, deque):
        return DoubleEndedQueue(SCREEN, ds)

    elif hasattr(ds, 'next') and hasattr(ds, 'val'):
        return LinkedList(ds)

    elif isinstance(ds, dict):
        return HashMap(SCREEN, ds)
    return

    # elif isinstance(ds, Array):
    #     return Array(ds)
