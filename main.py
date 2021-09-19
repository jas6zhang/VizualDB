import os
from collections import deque
import curses
from linked_list import Node, LinkedList
from debugger import debug

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sample(a, b):
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
    cool = TreeNode(1)
    cool.left = TreeNode(2)
    cool.right = TreeNode(3)
    cool.left.left = TreeNode(4)
    cool.left.right = TreeNode(5)
    debug(bin_tree, (cool, 3))
    #debug(sample, (2, 5))
