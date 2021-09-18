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
    # arr = []
    # for i in range(b):
    #     arr.append(a)
    # return arr
    q = deque()
    for i in range(b):
        q.append(a)
    return q


def bin_tree(root, n):
    curr = root.right
    for i in range(0, n, 2):
        curr.right = TreeNode(100 + i)
        curr.left = TreeNode(99 + i)
        curr = curr.right


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

    # debug(sample2, (Node1, 2))
    cool = TreeNode(1)
    cool.left = TreeNode(2)
    cool.right = TreeNode(3)
    cool.left.left = TreeNode(4)
    cool.left.right = TreeNode(5)
    debug(bin_tree, (cool, 3))
