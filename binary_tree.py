import math
import curses
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None, color=False, label=None):
        self.val = val
        self.left = left
        self.right = right
        self.color = color
        self.label = label


class BinaryTree:
    def __init__(self, screen, node):
        self.screen = screen
        self.root = node

    def dfs_remove_tags(self, node):
        node.color = False
        node.label = None
        if node.left:
            self.dfs_remove_tags(node.left)
        if node.right:
            self.dfs_remove_tags(node.right)

    def draw_circle(self, pos_x, pos_y, val, is_highlighted, label):
        r = 3
        for angle in range(0, 360, 5):
            x = r * 2 * math.sin(math.radians(angle)) + pos_x
            y = r * math.cos(math.radians(angle)) + pos_y
            if is_highlighted:
                self.screen.addstr(int(round(y)), int(round(x)), '*', curses.color_pair(3))
            else:
                self.screen.addstr(int(round(y)), int(round(x)), '*')

        if label:
            self.screen.addstr(pos_y + 4, pos_x - 2, label)

        self.screen.addstr(pos_y, pos_x, str(val))

    def draw_arrow(self, pos_x, pos_y, new_x, new_y):
        if pos_x < new_x:
            while pos_x < new_x:
                self.screen.addch(pos_y, pos_x, curses.ACS_BSBS)
                pos_x += 1
            self.screen.addch(pos_y, pos_x, curses.ACS_BBSS)
        else:
            while pos_x > new_x:
                self.screen.addch(pos_y, pos_x, curses.ACS_BSBS)
                pos_x -= 1
            self.screen.addch(pos_y, pos_x, curses.ACS_BSSB)
        pos_y += 1
        while pos_y < new_y:
            self.screen.addch(pos_y, pos_x, curses.ACS_SBSB)
            pos_y += 1

    def dfs_draw(self, node, pos_x, pos_y, depth, prev_x, prev_y):
        self.draw_circle(pos_x, pos_y, node.val, node.color, node.label)
        if prev_x > pos_x:
            self.draw_arrow(prev_x - 6, prev_y, pos_x, pos_y - 3)
        elif prev_x < pos_x:
            self.draw_arrow(prev_x + 6, prev_y, pos_x, pos_y - 3)

        if node.left:
            self.dfs_draw(node.left, pos_x - 5 * (6 - 2*depth), pos_y + 8, depth + 1, pos_x, pos_y)
        if node.right:
            self.dfs_draw(node.right, pos_x + 5 * (6 - 2*depth), pos_y + 8, depth + 1, pos_x, pos_y)

    def visualize(self):
        if self.root:
            y, x = self.screen.getmaxyx()
            self.dfs_draw(self.root, int(x/1.7), 7, 0, int(x/1.7), 7)
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
