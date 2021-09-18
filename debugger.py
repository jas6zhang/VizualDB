import inspect
import sys
from termcolor import cprint
import curses
from collections import deque

from vector import Vector
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue
from binary_tree import TreeNode, BinaryTree

SCREEN = curses.initscr()

print_blue = lambda x: cprint(x, 'blue')
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')

def print_trace(co, frame, source):
    SCREEN.clear()
    SCREEN.addstr(0, 0, co.co_name)
    SCREEN.addstr(1, 0, "Line #: " + str(frame.f_lineno))
    SCREEN.addstr(2, 0, "Locals: " + str(frame.f_locals))
    SCREEN.refresh()

    trees = []
    objects = []
    for val in frame.f_locals.values():
        items = check_type(val)
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
        else:
            objects.append(items)
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

def check_type(ds):
    if isinstance(ds, list):
        return Vector(ds)
    elif isinstance(ds, deque):
        return DoubleEndedQueue(SCREEN, ds)
    elif hasattr(ds, 'next') and hasattr(ds, 'val'):
        return LinkedList(ds)
    elif hasattr(ds, 'left') and hasattr(ds, 'right') and hasattr(ds, 'val'):
        return BinaryTree(SCREEN, ds)
    return

def visualization_factory(ds):
    if hasattr(ds, 'visualize'):
        ds.visualize()

