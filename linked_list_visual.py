import curses
import math
# draw the circle


def visualize(self):

    curr = self.head
    print(curr.val)
    while curr.next:
        print('->' + str(curr.next.val))
        curr = curr.next

    y_pos = 5
    y, x = self.screen.getmaxyx()

    box1 = self.screen.subwin(4, 20, y_pos, int(x/2))

    while cur:
        print(x)

    self.screen.addstr(y_pos + 2, int(x/2) + 10, str(node))
    box1.border(0)
    box1.box()
    y_pos += 4

    self.screen.refresh()


screen = curses.initscr()

curses.noecho()  # prevents user input from being echoed

# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update
# print(screen.getmaxyx())

# y, x = screen.getmaxyx()

# box1 = curses.newpad(y - 1, x - 1)
# box1.border(0)
# box2 = curses.newwin(4, 20, 5, int(x/2))
# box2.box()
# box3 = curses.newwin(4, 20, 8, int(x/2))
# box3.box()


def linked_list():

    a, b = 10, 10
    r = 3
    for angle in range(0, 360, 5):
        x = r * 2 * math.sin(math.radians(angle)) + a
        y = r * math.cos(math.radians(angle)) + b
        screen.addstr(int(round(y)), int(round(x)), '*')
    screen.addstr(int(math.floor((r + b)*.5+4)),
                  int(round(r + a + 5)), "»»------►")


linked_list()

screen.refresh()

curses.napms(5000)
curses.endwin()
print("hello")


# def main(stdscr):
#     stdscr.addstr(0, 0, "Enter IM message: (hi tCtrl-G to send)")

#     editwin = curses.newwin(5,30, 2,1)
#     rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
#     stdscr.refresh()

#     box = Textbox(editwin)

#     # Let the user edit until Ctrl-G is struck.
#     box.edit()

#     # Get resulting contents
#     message = box.gather()
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 11)), '\\')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 12)), '\\')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 13)), '\\')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 11)), '/')
# # screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 12)), '/')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 13)), '/')
# arrow
# screen.addstr(, int(round(x)), '-')
# screen.addstr(int(round(y)), int(round(x)), '-')

# screen.addstr(r+b+5, r+a+5, '-')
# screen.addstr(int(round(y)), int(round(x)), '*')

# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 3)), '-')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 6)), '-')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 7)), '-')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 8)), '-')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 9)), '-')
# screen.addstr(int(math.floor((r + b)*.5)), int(round(r + a + 10)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 5)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 6)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 7)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 8)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 9)), '-')
# screen.addstr(int(math.floor((r + b)*.5+1)), int(round(r + a + 10)), '-')

# screen.addstr(int(math.floor((r + b)*.5)),
#               int(round(r + a + 5)), '              .')
