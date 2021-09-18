import curses, curses.panel
import time as t

screen = curses.initscr()

# screen.border(0)
print(screen.getmaxyx())

y, x = screen.getmaxyx()

box1 = screen.subwin(y - 1, x - 1, 0, 0)
box1.border(0)
box1.box()

box2 = screen.subwin(4, 20, 5, int(x/2))
box2.border(0)
box2.box()
box3 = screen.subwin(4, 20, 9, int(x/2))
box3.border(0)
box3.box()

screen.refresh()

curses.napms(3000)
curses.endwin()
