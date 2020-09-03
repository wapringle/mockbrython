# mockbrython
Mock brython functions for local testing and debugging.
Brython is designed to enable python as a scripting language for the Web. When developing applications it is useful to test for syntax errors and debug logic before loading web pages. This small collection of files enables this. It blanks off all the brython-specific calls to enable the python interpreter to syntax scan the script, and allows a debugger to test the logic. Obviously it doesn't do much for the web-specific part of your design, but it means that the logic is fairly sound when the pages are loaded.

At first sight, this is fairly trivial, but it took some effort to get right, so I felt it worth publishing

Clone this directory to a directory OUTSIDE the script you are developing and add this directory to PYTHONPATH
eg

$ export PYTHONPATH=${PYTHONPATH}:${HOME}/mockbrython

then running a script containing brython calls will catch syntax errors without hitting unresolved brython calls
$ python devel_script.py

The script can also be debugged using idle, our your IDE of choice
