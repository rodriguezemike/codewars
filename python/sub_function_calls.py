'''
The aim of this kata is to determine the number of sub-function calls made by an unknown function.

You have to write a function named count_calls which:

takes as parameter a function and its arguments (args, kwargs)

calls the function

returns a tuple containing:

the number of function calls made inside it and inside all the sub-called functions recursively

the function return value.

NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.
'''
import sys

COUNTER = 0
funcs = ['assert', 'format', 'expect', 'display']

def count(frame, event, arg):
    global COUNTER
    func_name = frame.f_code.co_name
    if event == 'call':
        for f in funcs:
            if f in func_name:
                break
        else:
            COUNTER += 1
        return count
    return 

def count_calls(func, *args, **kwargs):
    global call_func
    global COUNTER
    COUNTER = 0
    sys.settrace(count)
    value = func(*args,**kwargs)
    return (COUNTER - 1, value)


def count_calls_proper(func, *args, **kwargs):
    counter = 0
    
    def count(frame, event, arg):
        nonlocal counter
        if event == 'call':
            counter += 1
        return count 
    
    sys.settrace(count)
    value = func(*args,**kwargs)
    return (counter - 1, value)
