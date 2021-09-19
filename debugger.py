import inspect
import sys
import curses

from vector import Vector
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue
from binary_tree import TreeNode, BinaryTree
from visualization_factory import check_type, visualization_factory


SCREEN = curses.initscr()

# print_blue = lambda x: cprint(x, 'blue')
# print_red = lambda x: cprint(x, 'red')
# print_green = lambda x: cprint(x, 'green')


def print_trace(co, frame, source):
    SCREEN.clear()
    SCREEN.addstr(0, 0, "Locals: " + str(frame.f_locals))
    curr = 2
    #curr_line_no = frame.f_lineno
    curr_line_no = co.co_firstlineno
    for line in source:
        SCREEN.addstr(curr, 0, str(curr_line_no))
        SCREEN.addstr(curr, 4, line)
        if curr_line_no == frame.f_lineno:
            SCREEN.addstr(curr, 4 + len(line) + 1, "<--")
        curr += 1
        curr_line_no += 1
    SCREEN.refresh()

    trees = []
    objects = []
    ll = []
    for val in frame.f_locals.values():
        items = check_type(val, SCREEN)
        if isinstance(items, BinaryTree):
            if len(trees) == 0:
                trees.append(items)
            else:
                for i in range(len(trees)):
                    if trees[i].validate(items):
                        break
                    if items.validate(trees[i]):
                        trees[i] = items
                        break
                    if i == len(trees) - 1:
                        trees.append(items)
        elif isinstance(items, LinkedList):

            if len(ll) == 0:
                ll.append(items)
            objects.append(items)

        else:
            objects.append(items)

    for l in ll:
        objects.append(l)
    for tree in trees:
        objects.append(tree)
    for obj in objects:
        visualization_factory(obj)


def trace_lines(frame, event, arg):
    if event != 'line' and event != 'return':
        curses.endwin()
        exit()
        return

    co = frame.f_code
    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    y, x = SCREEN.getmaxyx()
    cmd = SCREEN.getch(y - 1, 0)

    if cmd == ord("s"):
        return trace_lines

    if cmd == ord("q"):
        curses.endwin()
        exit()
        return

    if cmd == ord("o"):
        return trace_calls


def trace_calls(frame, event, arg):
    if event != 'call':
        curses.endwin()
        exit()
        return

    co = frame.f_code
    func_name = co.co_name

    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    y, x = SCREEN.getmaxyx()
    cmd = SCREEN.getch(y - 1, 0)

    if cmd == ord('s'):
        return trace_lines

    if cmd == ord('q'):
        curses.endwin()
        exit()
        return

    if cmd == ord('o'):
        return

    return


def debug(fn, args):
    sys.settrace(trace_calls)
    fn(*args)
