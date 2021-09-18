class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, screen, node):
        self.screen = screen
        self.head = node

    def visualize(self):
        curr = self.head
        self.screen.border(0)

        def linked_list():

            a, b = 10, 10
            r = 3
            for angle in range(0, 360, 5):
                x = r * 2 * math.sin(math.radians(angle)) + a
                y = r * math.cos(math.radians(angle)) + b
                screen.addstr(int(round(y)), int(round(x)), '*')

            screen.addstr(int(round(y)), int(round(x), curr))

        # draw arrow

        screen.addstr(int(math.floor((r + b)*.5+4)),
                      int(round(r + a + 5)), "»»------►")

    print(curr.val)
    while curr.next:
        print('->' + str(curr.next.val))
        curr = curr.next
