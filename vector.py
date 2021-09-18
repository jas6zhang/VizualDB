class Vector:
    def __init__(self, screen, arr):
        self.val = arr
        self.screen = screen

    def visualize(self):
        i = 0
        # figure out max width to get halfway point
        y, x = self.screen.getmaxyx()
        for elem in self.val:
            # start array at half way point
            box1 = self.screen.subwin(5, 5, 5, int(x/2) + i*5)
            # print the elements in each box
            self.screen.addstr(7, int(x/2) + 1 + i*5, str(elem))
            box1.border(0)
            box1.box()
            # to work on windows
            box1.refresh()
            i += 1

        self.screen.refresh()
