import curses
import math
# draw the circle

screen = curses.initscr()

curses.noecho()  # prevents user input from being echoed

curses.cbreak()

# Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)")
# screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")

# screen.addch(0, 0, "X")
# screen.addch(0, 1, "X")
# screen.addch(0, 2, "X")

# screen.addch(0, 3, "X")

# screen.addch(0, 4, "X")
# screen.addch(0, 5, "X")
# screen.addch(0, 6, "X")
# screen.addch(0, 7, "X")
# screen.addch(0, 8, "X")

# screen.addch(0, 0, "X")
# screen.addch(1, 0, "X")
# screen.addch(2, 0, "X")

# screen.addch(3, 0, "X")

# screen.addch(4, 0, "X")
# screen.addch(5, 0, "X")
# screen.addch(6, 0, "X")
# screen.addch(7, 0, "X")
# screen.addch(8, 0, "X")

# screen.addch(0, 0, "-")
# screen.addch(0, 1, "-")
# screen.addch(0, 2, "-")

# screen.addch(0, 3, "X")

# screen.addch(0, 4, "X")
# screen.addch(0, 5, "X")
# screen.addch(0, 6, "X")
# screen.addch(0, 7, "X")
# screen.addch(0, 8, "X")

# screen.addch(0, 0, "X")
# screen.addch(1, 0, "X")
# screen.addch(2, 0, "X")

# screen.addch(3, 0, "X")

# screen.addch(4, 0, "X")
# screen.addch(5, 0, "X")
# screen.addch(6, 0, "X")
# screen.addch(7, 0, "X")
# screen.addch(8, 0, "X")


def draw_piece(screen, x_center, y_center, radius):

    screen.addstr(y_center + radius, x_center + radius, '*')
    screen.addstr(y_center + radius, x_center - radius, '*')
    screen.addstr(y_center - radius, x_center + radius, '*')
    screen.addstr(y_center - radius, x_center - radius, '*')
    screen.addstr(y_center + radius, x_center + radius, '*')
    screen.addstr(y_center + radius, x_center - radius, '*')
    screen.addstr(y_center - radius, x_center + radius, '*')
    screen.addstr(y_center - radius, x_center - radius, '*')

    x = 0
    y = radius
    d = 3 - 2 * radius
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6
        draw_piece(screen, x, y, radius)


# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update

# draw_piece(screen, 10, 10, 5)
def linked_list() {

    a, b = 10, 10
    r = 8
    for angle in range(0, 360, 5):
        x = r * math.sin(math.radians(angle)) + a
        y = r * math.cos(math.radians(angle)) + b
        screen.addstr(int(round(y)), int(round(x)), '*')

    screen.addstr(r+b+5, r+a+5, '-')
    screen.addstr(int(round(y)), int(round(x)), '*')
}


def arrow() {
    # screen.addstr(int(round(y)), int(round(x)), '*')
    # screen.addstr(int(round(y)), int(round(x)), '*')
}


screen.refresh()

curses.napms(10000)
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
