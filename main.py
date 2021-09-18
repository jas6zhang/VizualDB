import os
from collections import deque
import curses
from debugger import debug


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sample(a, b):
    # arr = []
    # for i in range(b):
    #     arr.append(a)
    # return arr
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


def sample2(Node1, wtf):
    curr = Node1

    while curr.next:
        curr = curr.next

    for i in range(2):
        Node4 = Node(4)

        curr.next = Node4
        curr = curr.next


if __name__ == "__main__":
    os.system('color')
    curses.start_color()
    curses.echo()

    Node1 = Node(1)

    Node2 = Node(2)

    Node3 = Node(3)

    Node1.next = Node2
    Node2.next = Node3

    debug(sample2, (Node1, 2))
