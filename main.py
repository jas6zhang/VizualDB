import os
from collections import deque
import curses

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
