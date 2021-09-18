class Vector:
    def __init__(self, screen, arr):
        self.val = arr
        self.screen = screen

    def visualize(self):
        # print(self.val, "CALLED")
        # y, x = self.screen.getmaxyx()
        i = 0
        for x in self.val:
            print(x)
            self.screen.border(0)
            box1 = self.screen.subwin(5 + i*5, 5 + i*5, 5, 5)
            self.screen.addstr(5 + i*5, 5 + i*5, str(x))
            box1.box()
            self.screen.getch()
            i += 1

        self.screen.refresh()
