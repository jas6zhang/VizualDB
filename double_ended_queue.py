class DoubleEndedQueue:
    def __init__(self, screen, q):
        self.queue = q
        self.screen = screen

    def visualize(self):
        y_pos = 5
        y, x = self.screen.getmaxyx()
        for elem in self.queue:
            box1 = self.screen.subwin(4, 20, y_pos, int(x/2))
            self.screen.addstr(y_pos + 2, int(x/2) + 10, str(elem))
            box1.border(0)
            box1.refresh()
            y_pos += 4
        self.screen.refresh()

