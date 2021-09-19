from collections import deque

from vector import Vector
from hash_map import HashMap
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue
from binary_tree import TreeNode, BinaryTree


def check_type(ds, screen):
    if isinstance(ds, list):
        return Vector(ds)
    elif isinstance(ds, deque):
        return DoubleEndedQueue(screen, ds)
    elif hasattr(ds, 'next') and hasattr(ds, 'val'):
        return LinkedList(ds)
    elif hasattr(ds, 'left') and hasattr(ds, 'right') and hasattr(ds, 'val'):
        return BinaryTree(screen, ds)
    return


def visualization_factory(ds):
    if hasattr(ds, 'visualize'):
        ds.visualize()
