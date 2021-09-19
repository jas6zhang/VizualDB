class Vector:
    def __init__(self, screen, arr):
        self.val = arr
        self.screen = screen

    def visualize(self):
        i = 0
        y, x = self.screen.getmaxyx()
        for elem in self.val:
            box1 = self.screen
            if isinstance(elem, list):
                box1 = self.screen.subwin(5, 10, 40, int(x/2) + i*10)
                self.screen.addstr(42, int(x/2) + 2 + i*10, str(elem))
            else:
                # start array at half way point
                box1 = self.screen.subwin(5, 10, 5, int(x/2) + i*10)
                # print the elements in each box
                self.screen.addstr(7, int(x/2) + 3 + i*10, str(elem))

            box1.border(0)
            box1.box()
                # to work on windows
            box1.refresh()
            i += 1

        self.screen.refresh()
