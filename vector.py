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
# for elem in self.queue:
#             box1 = self.screen.subwin(4, 20, y_pos, int(x/2))
#             self.screen.addstr(y_pos + 2, int(x/2) + 10, str(elem))
#             box1.border(0)
#             box1.box()
#             y_pos += 4
