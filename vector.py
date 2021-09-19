class Vector:
    def __init__(self, screen, arr):
        self.val = arr
        self.screen = screen

    def visualize(self):
<<<<<<< HEAD
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
=======
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
>>>>>>> 4b3b41ae8f15681f79cfaa378ab6636e26e8040f
            i += 1

        self.screen.refresh()
