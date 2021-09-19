import math
import curses


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, screen, node):
        self.screen = screen
        self.head = node

    def visualize(self):
        curr = self.head
        iteration = 0

        while curr:
            self.linked_list(curr.val, iteration)
            iteration += 1
            curr = curr.next

        self.screen.refresh()

    def linked_list(self, curr, iteration):

        y, x = self.screen.getmaxyx()
        a, b = 10, int(x/3)  # y,x
        r = 3

        if iteration > 0:
            self.screen.addstr(int(math.floor((r + a)*.5+4)),
                               int(round(b-r - 9) + 20 * iteration), "-----►", curses.color_pair(3))

        for angle in range(0, 360, 5):
            x = r * 2 * math.sin(math.radians(angle)) + b + 20 * iteration
            y = r * math.cos(math.radians(angle)) + a
            self.screen.addstr(int(round(y)), int(
                round(x)), '*', curses.color_pair(3))

        # if curr == node4:
        #     ye
        # else:
        self.screen.addstr(a, b + 20 * iteration, str(curr))
