"""
Mock brython functions for local testing and debugging.

Copy this directory to a directory OUTSIDE the script you are developing and add this directory to PYTHONPATH
eg

$ export PYTHONPATH=${PYTHONPATH}:${HOME}/brython

then running a script containing brython calls will catch syntax errors without hitting unresolved brython calls
$ python devel_script.py

The script can also be debugged using idle, our your IDE of choice
"""

from browser.html import _htmltype, _htmltype1

document = _htmltype1()

def alert(*args, **kwargs):
    pass

def bind(target, evt):
    def decorator(func):
        def wrapper(target, evt) :
            return target.bind(func,evt)
        return wrapper
    return decorator





