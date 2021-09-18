from vector import Vector
from linked_list import Node, LinkedList


def visualization_factory(ds):
    if hasattr(ds, 'visualize'):
        ds.visualize()


def check_type(ds):
    if isinstance(ds, list):
        return Vector(ds)
    elif isinstance(ds, Node):
        return LinkedList(ds)
    return
