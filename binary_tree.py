import math
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, screen, node):
        self.screen = screen
        self.root = node

    def draw_circle(self, pos_x, pos_y, val):
        r = 3
        for angle in range(0, 360, 5):
            x = r * 2 * math.sin(math.radians(angle)) + pos_x
            y = r * math.cos(math.radians(angle)) + pos_y
            self.screen.addstr(int(round(y)), int(round(x)), '*')
        self.screen.addstr(pos_y, pos_x, str(val))

    def draw_arrow(self):
        pass

    def dfs_draw(self, node, pos_x, pos_y, depth):
        self.draw_circle(pos_x, pos_y, node.val)

        if node.left:
            self.dfs_draw(node.left, pos_x - 6 * (8 - 2*(depth + 1)), pos_y + 7, depth + 1)
        if node.right:
            self.dfs_draw(node.right, pos_x + 6 * (8 - 2*(depth + 1)), pos_y + 7, depth + 1)

    def visualize(self):
        if self.root:
            y, x = self.screen.getmaxyx()
            self.dfs_draw(self.root, int(x/2), 7, 0)
            self.screen.refresh()

    def is_subtree(self, s, t):
        if not s:
            return False
        if self.is_same_tree(s, t):
            return True
        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_same_tree(self, p, q):
        if p and q:
            return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        return p is q

    def validate(self, tree):
        return self.is_subtree(self.root, tree.root)
