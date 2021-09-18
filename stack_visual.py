import curses
import curses.panel

screen = curses.initscr()

# screen.border(0)
print(screen.getmaxyx())

y, x = screen.getmaxyx()

box1 = curses.newpad(y - 1, x - 1)
box1.border(0)
box2 = curses.newwin(4, 20, 5, int(x/2))
box2.box()
box3 = curses.newwin(4, 20, 8, int(x/2))
box3.box()
curses.panel.new_panel(box2)
curses.panel.new_panel(box3)

# screen.refresh()
#box2.refresh(2, int(x/2), 0, 0, 4, 15)
curses.panel.update_panels()
box1.refresh(0, 0, 0, 0, y - 1, x - 1)
curses.doupdate()
# box2.refresh()
# box3.refresh()

curses.napms(3000)
curses.endwin()
