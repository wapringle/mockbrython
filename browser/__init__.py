"""
Mock brython functions for local testing and debugging.

Copy this directory to a directory OUTSIDE the script you are developing and add this directory to PYTHONPATH
eg

$ export PYTHONPATH=${PYTHONPATH}:${HOME}/brython

then running a script containing brython calls will catch syntax errors without hitting unresolved brython calls
$ python devel_script.py

The script can also be debugged using idle, our your IDE of choice
"""

from browser.html import _htmltype

class _htmltype1(dict):
    items = []

    def __le__(self, other):
        self.items.append(other)

    def __missing__(self, attr):
        return _htmltype()

    def __getattr__(self, attr):
        return 0

    def __setattr__(self, attr, value):
        pass

document = _htmltype1()

def alert(*args, **kwargs):
    pass




