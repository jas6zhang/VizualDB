import curses 

class HashMap:
    def __init__(self, screen, hash_map):
        self.hash_map = hash_map
        self.screen = screen

    def visualize(self):
        y, x = self.screen.getmaxyx()
        i = 0
        for key in self.hash_map:

            box1 = self.screen.subwin(
                5, 10, 10 + 5*i, int(x/2))
            self.screen.addstr(12 + 5*i, 4 + int(x/2), str(key))

            self.screen.addstr(12 + 5*i, 11 + int(x/2), str("»»=====>"))

            box2 = self.screen.subwin(
<<<<<<< HEAD
                5, 10, 5 + 5*i, int(x/2) + 20)
            self.screen.addstr(7 + 5*i, 23 + int(x/2), str(self.hash_map[key]))
=======
                5, 10, 10 + 5*i, int(x/2) + 20)
            self.screen.addstr(12 + 5*i, 23 + int(x/2), str(self.hash_map[key]))
>>>>>>> d9bc87edb96de5d2487a8398c03e302f051ce4ce

            box1.border(0)
            box1.box()
            box2.border(0)
            box2.box()
            i += 1
            box1.refresh()
            box2.refresh()

        self.screen.refresh()
