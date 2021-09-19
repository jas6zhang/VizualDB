import inspect
import sys
import curses

from vector import Vector
from linked_list import Node, LinkedList
from double_ended_queue import DoubleEndedQueue
from binary_tree import TreeNode, BinaryTree
from visualization_factory import check_type, visualization_factory


SCREEN = curses.initscr()


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
    lll = []
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
            lll.append(items)
            if len(ll) == 0:
                ll.append(items)

            objects.append(items)

        else:
            objects.append(items)

    compare_lists(lll)
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

def compare_lists(lll):
    for i in range(1, len(lll)):
        lll[i].head.color = False

    if len(lll) > 0:
        curr = lll[0].head

        while curr:
            curr.color = False
            for i in range(1, len(lll)):
                if id(curr) == id(lll[i].head):
                    lll[i].head.color = True

            curr = curr.next


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
