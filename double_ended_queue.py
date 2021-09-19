import curses

class DoubleEndedQueue:
    def __init__(self, screen, q):
        self.queue = q
        self.screen = screen

    def visualize(self):
        y_pos = 28
        y, x = self.screen.getmaxyx()
        for elem in self.queue:
<<<<<<< HEAD
            box = self.screen.subwin(
                4, 20, y_pos, int(x/2))
            self.screen.addstr(y_pos + 2, int(x/2) + 10, str(elem) )
=======
            box = self.screen.subwin(4, 20, y_pos, int(x/2))
            self.screen.addstr(y_pos + 2, int(x/2) + 10, str(elem.val))
>>>>>>> d9bc87edb96de5d2487a8398c03e302f051ce4ce
            box.border(0)
            box.refresh()
            y_pos += 4
        self.screen.refresh()
