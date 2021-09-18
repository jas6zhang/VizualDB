import os
from collections import deque
import curses
from linked_list import Node, LinkedList
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


def sample3(a, b):
    hash_map = {1: "Bob"}
    hash_map[3] = "John"
    hash_map[5] = "Ross"
    return hash_map

# def sample2():
#     head = Node(1)
#     llist = LinkedList(head)
#     llist.addNode(2)
#     llist.addNode(3)
#     llist.addNode(4)
#     llist.visualize()


if __name__ == "__main__":
    os.system('color')
    curses.start_color()
    curses.echo()
    # note: only one function can work at at time (i.e. overlap can occur)
    # debug(sample, (2, 5))
    # debug(sample1, (3, 5))

    debug(sample3, (1, 2))
