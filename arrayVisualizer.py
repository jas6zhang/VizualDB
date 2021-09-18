import curses
stdscr = curses.initscr() # initializing the terminal

curses.noecho() # prevent key echoing, and only display them for certain circumstance
curses.cbreak() # to react to certain keys without enter
stdscr.keypad(True) # to let curses return special keys





# Terminate curses
curses.echo()
curses.nocbreak()
stdscr.keypad(False)

# revert back from curses-based terminal
curses.endwin()


def main():

if __name__ = '__main__':
	main()