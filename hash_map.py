class HashMap:
    def __init__(self, screen, hash_map):
        self.hash_map = hash_map
        self.screen = screen

    def visualize(self):
        i = 0
        print(len(self.hash_map))
        for key in self.hash_map:

            box1 = self.screen.subwin(5, 10, 5 + 5*i, 5)
            self.screen.addstr(7 + 5*i, 8, str(key))

            self.screen.addstr(7 + 5*i, 16, str("»»=====>"))

            box2 = self.screen.subwin(5, 10, 5 + 5*i, 25)
            self.screen.addstr(7 + 5*i, 27, str(self.hash_map[key]))

            box1.border(0)
            box1.box()
            box2.border(0)
            box2.box()
            i += 1
            box1.refresh()
            box2.refresh()

        self.screen.refresh()
