import inspect
import sys
import curses
import time
from vector import Vector
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue
from binary_tree import TreeNode, BinaryTree
from visualization_factory import check_type, visualization_factory

SCREEN = curses.initscr()
global breakpoints
breakpoints = []


def search(x, arr):
    a = 0
    for i in arr:
        if a == 0:
            a += 1
            continue
        if int(x) == int(i):
            return True
    return False


def print_trace(co, frame, source):
    SCREEN.clear()
    SCREEN.addstr(0, 0, "Locals: " + str(frame.f_locals))

    curr = 2
    curr_line_no = co.co_firstlineno
    for line in source:
        if curr_line_no == frame.f_lineno:
            SCREEN.addstr(curr, 0, str(curr_line_no), curses.color_pair(7))
            SCREEN.addstr(curr, 4, line, curses.color_pair(7))
            SCREEN.addstr(curr, 4 + len(line) + 1, "<--", curses.color_pair(7))
        else:
            SCREEN.addstr(curr, 0, str(curr_line_no))
            SCREEN.addstr(curr, 4, line)

        curr += 1
        curr_line_no += 1
    SCREEN.refresh()

    trees = []
    objects = []
    ll = []

    lll = {}
    highlight_trees = {}
    for key, val in frame.f_locals.items():
        items = check_type(val, SCREEN)
        if isinstance(items, BinaryTree):
            if len(trees) == 0:
                trees.append(items)
            else:
                for i in range(len(trees)):
                    if trees[i].validate(items):
                        highlight_trees[items] = key
                        break
                    if items.validate(trees[i]):
                        highlight_trees[trees[i]] = key
                        trees[i] = items
                        break
                    if i == len(trees) - 1:
                        trees.append(items)
        elif isinstance(items, LinkedList):
            if len(ll) == 0:
                ll.append(items)

            else:
                lll[val] = key

            objects.append(items)

        else:
            objects.append(items)

    compare_lists(lll, ll)
    color_trees(highlight_trees, trees)

    for l in ll:
        objects.append(l)
    for tree in trees:
        objects.append(tree)

    for obj in objects:
        visualization_factory(obj)


def color_trees(tree_map, tree_list):
    for tree in tree_list:
        if tree.root:
            tree.dfs_remove_tags(tree.root)
    for tree in tree_map.keys():
        tree.root.color = True
        tree.root.label = tree_map[tree]


def compare_lists(lll, ll):
    for i in lll.keys():
        i.color = False
        i.label = None

    if len(ll) > 0:
        curr = ll[0].head

        while curr:
            curr.color = False
            curr.label = None

            for i in lll.keys():
                if id(curr) == id(i):
                    i.color = True
                    i.label = lll[i]

            curr = curr.next


def setCheckpoints(frame, event, arg):
    global breakpoints
    y, x = SCREEN.getmaxyx()
    lines = SCREEN.getstr(y - 1, 2)
    breakpoints = lines.decode().split(" ")
    i = 0
    for line in breakpoints:
        if i == 0:
            i += 1
            continue
    print(breakpoints)
    cmd = SCREEN.getch(y - 1, len(lines))

    # print(breakpoints)
    if cmd == ord('q') or search(frame.f_lineno, breakpoints):
        SCREEN.addstr(1, 0, "BREAKPOINT FOUND")
        curses.endwin()
        # exit()
        return

    if cmd == ord("s"):
        return trace_lines

    if cmd == ord("o"):
        return trace_calls


def trace_lines(frame, event, arg):
    global breakpoints
    # if event != 'line' and event != 'return':
    #     curses.endwin()
    #     exit()
    #     return

    co = frame.f_code
    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)
    y, x = SCREEN.getmaxyx()
    cmd = SCREEN.getch(y - 1, 0)
    # print(breakpoints)
    search(frame.f_lineno, breakpoints)

    if search(frame.f_lineno, breakpoints):
        SCREEN.addstr(1, 0, "BREAKPOINT FOUND")
        SCREEN.refresh()
        exit()
        return

    if cmd == ord('q'):
        curses.endwin()
        exit()
        return

    if cmd == ord("s"):
        return trace_lines

    if cmd == ord("o"):
        return trace_calls

    if cmd == ord('b'):
        return setCheckpoints


def trace_calls(frame, event, arg):
    global breakpoints
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

    search(frame.f_lineno, breakpoints)
    time.sleep(2)
    if cmd == ord('q') or search(frame.f_lineno, breakpoints):
        curses.endwin()
        exit()
        return

    if cmd == ord('s'):
        return trace_lines

    if cmd == ord('o'):
        return

    if cmd == ord('b'):
        setCheckpoints(frame, event, arg)

    return


def debug(fn, args):
    curses.start_color()

    curses.use_default_colors()

    curses.init_pair(1, 200, -1)  # array color ---> Yellow
    curses.init_pair(2, 230, -1)  # linked list color --> Pink/Red
    curses.init_pair(3, 47, -1)  # stack / queue color --> Neon Green
    curses.init_pair(4, 180, -1)  # hashmap color --> Orange
    curses.init_pair(5, 142, -1)  # heap color ---> Purple
    curses.init_pair(6, 150, -1)  # binary tree color ---> Blue

    curses.init_pair(7, 14, -1)  # binary tree color ---> Arrow + Line Number

    curses.echo()

    sys.settrace(trace_lines)
    fn(*args)
