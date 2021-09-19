import os
from collections import deque
import curses
from debugger import debug


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sample(a, b):
    q = deque()
    for i in range(b):
        q.append(a)
    return q


def bin_tree(root, n):
    curr = root.right
    for i in range(0, n, 2):
        curr.right = TreeNode(5 + i)
        curr.left = TreeNode(6 + i)
        curr = curr.right


def sample1(a, b):  # array
    arr = []
    i = 0
    for i in range(b):
        arr.append(i)
        i += 1
    return arr


def sample2(Node1, next):  # linked list
    curr = Node1

    while curr.next:
        curr = curr.next

    for i in range(2):
        Node4 = Node(4)

        curr.next = Node4
        curr = curr.next


def sample3(a, b):  # hashmap
    hash_map = {1: "Bob"}
    hash_map[3] = "John"
    hash_map[5] = "Ross"
    return hash_map


if __name__ == "__main__":
    os.system('color')
    curses.start_color()

    curses.use_default_colors()

    curses.init_pair(1, 200, -1)  # array color ---> Yellow
    curses.init_pair(2, 230, -1)  # stack / queue color  --> Pink/Red
    curses.init_pair(3, 47, -1)  # linked list color --> Neon Green
    curses.init_pair(4, 180, -1)  # hashmap color --> Oranges
    curses.init_pair(6, 150, -1)  # binary tree color ---> Blue

    curses.init_pair(7, 14, -1)  # binary tree color ---> Arrow + Line Number

    curses.echo()

    Node1 = Node(1)

    Node2 = Node(2)

    Node3 = Node(3)

    Node1.next = Node2
    Node2.next = Node3

    debug(sample2, (Node1, 2))

    # debug(sample1(a, b):
    # cool = TreeNode(1)
    # cool.left = TreeNode(2)
    # cool.right = TreeNode(3)
    # cool.left.left = TreeNode(4)
    # cool.left.right = TreeNode(5)
    # debug(bin_tree, (cool, 3))
    # note: only one function can work at at time (i.e. overlap can occur)
    # debug(sample, (2, 5))
    # debug(sample1, (3, 5))

    # debug(sample3, (1, 2)) --> Hash Map

    cool = TreeNode(1)
    cool.left = TreeNode(2)
    cool.right = TreeNode(3)
    cool.left.left = TreeNode(4)
    cool.left.right = TreeNode(5)
    # debug(bin_tree, (cool, 3))

    # debug(sample, (2, 5))
    # debug(sample1, (2, 3))
    # debug(sample3, (2, 3))
