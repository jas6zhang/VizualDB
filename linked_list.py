import math
import curses


class Node:
    def __init__(self, val, next, color=False, label=None):
        self.val = val
        self.next = None
        self.color = color
        self.label = label


class LinkedList:
    def __init__(self, screen, node):
        self.screen = screen
        self.head = node

    def visualize(self):
        curr = self.head
        iteration = 0

        while curr:
            self.display(curr, iteration)
            iteration += 1
            curr = curr.next

        self.screen.refresh()

    def display(self, curr, iteration):

        y, x = self.screen.getmaxyx()
        a, b = 10, int(x/3)  # y,x
        r = 3

        if iteration > 0:
            self.screen.addstr(int(math.floor((r + a)*.5+4)),
                               int(round(b-r - 9) + 20 * iteration), "-----►")

        if hasattr(curr, "color") and curr.color:
            for angle in range(0, 360, 5):
                x = r * 2 * math.sin(math.radians(angle)) + b + 20 * iteration
                y = r * math.cos(math.radians(angle)) + a

                self.screen.addstr(int(round(y)), int(
                    round(x)), '*', curses.color_pair(3))
            self.screen.addstr(a, b + 20 * iteration, str(curr.val))

        else:
            self.screen.addstr(a, b + 20 * iteration, str(curr.val))

            for angle in range(0, 360, 5):
                x = r * 2 * math.sin(math.radians(angle)) + b + 20 * iteration
                y = r * math.cos(math.radians(angle)) + a

                self.screen.addstr(int(round(y)), int(
                    round(x)), '*')

        if hasattr(curr, "label") and curr.label:
            self.screen.addstr(a + 5, b - 2 + 20 * iteration, curr.label)
            #self.screen.addstr(a+8, b - 2 + 20 * iteration, str(curr.val))

        else:
            #self.screen.addstr(a+8, b - 2 + 20 * iteration, str(curr.val))
            self.screen.addstr(a + 5, b - 2 + 20 * iteration, "     ")
