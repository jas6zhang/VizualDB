import inspect
import multiprocessing
import sys
from termcolor import cprint

from visualization_factory import visualization_factory, check_type


def print_blue(x): return cprint(x, 'blue')
def print_red(x): return cprint(x, 'red')
def print_green(x): return cprint(x, 'green')


class StopExecution(Exception):
    pass


def print_trace(co, frame, source):
    #print("File", co.co_filename)
    #print("Name", co.co_name)
    # print("Line#", str(frame.f_lineno))
    # print("")
    # print("frame")
    print_green(co.co_name)
    print_red("Line #: " + str(frame.f_lineno))
    # print("First Line#", co.co_firstlineno)
    print_blue("Locals: " + str(frame.f_locals))
    #print_green("Source: " + str(source))
    # for line in source:
    #     print_green(line)

    for val in frame.f_locals.values():
        visualization_factory(check_type(val))


def trace_lines(frame, event, arg):
    if event != 'line' and event != 'return':
        return

    co = frame.f_code
    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    #cmd = trace_lines.debugq.get()
    cmd = input()

    if cmd == "step":
        return trace_lines

    if cmd == "quit":
        exit()
        return

    if cmd == "over":
        return trace_calls


def trace_calls(frame, event, arg):
    if event != 'call':
        return

    co = frame.f_code
    func_name = co.co_name

    source = inspect.getsourcelines(co)[0]

    print_trace(co, frame, source)

    #cmd = trace_lines.debugq.get()
    cmd = input()

    if cmd == 'step':
        return trace_lines

    if cmd == 'over':
        return

    return


def debug(fn, args):
    #trace_lines.debugq = debugq
    #trace_lines.applicationq = applicationq

    sys.settrace(trace_calls)

    fn(*args)


# if __name__ == "__main__":
    # sys.settrace(trace_calls)
    # sample(3, 2)

    #applicationq = multiprocessing.Queue()
    #debugq = multiprocessing.Queue()

    #debug_process = multiprocessing.Process(target=debug, args=(applicationq, debugq, sample, (2, 3)))
    #debug(applicationq, debugq, sample, (2, 3))
    # debug_process.start()
