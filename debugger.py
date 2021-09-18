import inspect
import sys
from termcolor import cprint
import curses

from visualization_factory import visualization_factory, check_type, SCREEN


def print_blue(x): return cprint(x, 'blue')
def print_red(x): return cprint(x, 'red')
def print_green(x): return cprint(x, 'green')


def print_trace(co, frame, source):
    #print("File", co.co_filename)
    #print("Name", co.co_name)
    # print("Line#", str(frame.f_lineno))
    # print("")
    # print("frame")
    SCREEN.addstr(0, 0, co.co_name)
    SCREEN.addstr(1, 0, "Line #: " + str(frame.f_lineno))
    SCREEN.addstr(2, 0, "Locals: " + str(frame.f_locals))
    SCREEN.refresh()
    # print_green(co.co_name)
    # print_red("Line #: " + str(frame.f_lineno))
    # #print("First Line#", co.co_firstlineno)
    # print_blue("Locals: " + str(frame.f_locals))
    #print_green("Source: " + str(source))
    # for line in source:
    #     print_green(line)

    for val in frame.f_locals.values():
        visualization_factory(check_type(val))


def trace_lines(frame, event, arg):
    if event != 'line' and event != 'return':
        curses.endwin()
        return

    co = frame.f_code
    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    #cmd = trace_lines.debugq.get()
    y, x = SCREEN.getmaxyx()
    cmd = SCREEN.getch(y - 1, 0)

    if cmd == ord("s"):
        return trace_lines

    if cmd == ord("q"):
        curses.endwin()
        return

    if cmd == ord("o"):
        return trace_calls


def trace_calls(frame, event, arg):
    if event != 'call':
        curses.endwin()
        return

    co = frame.f_code
    func_name = co.co_name

    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    #cmd = trace_lines.debugq.get()
    y, x = SCREEN.getmaxyx()
    cmd = SCREEN.getch(y - 1, 0)

    if cmd == ord('s'):
        return trace_lines

    if cmd == ord('q'):
        curses.endwin()
        return

    if cmd == ord('o'):
        return

    return


def debug(fn, args):
    #trace_lines.debugq = debugq
    #trace_lines.applicationq = applicationq

    sys.settrace(trace_calls)

    fn(*args)
