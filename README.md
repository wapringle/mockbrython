# mockbrython
Mock brython functions for local testing and debugging.

Brython is designed to enable python as a scripting language for the Web. Python scripts are uploaded to a web browser and interpreted by the Brython interpreter that is uploaded along with the python scripts. There are a number of Brython modules that provide web-specific functions to create the web page which are implemented by the interpreter.

When developing applications it is useful to test for syntax errors and debug logic before loading web pages. This small collection of files enables this. They provide a set of dummy modules that mirror the Brython modules, but blank off all the Brython-specific calls to enable the python interpreter to syntax scan the scripts and enable a debugger to exercise the logic. Obviously it doesn't do much for the web-specific part of your design, but it means that the logic is fairly sound when the pages are loaded. Also, an IDE source assistant can use the definitions to prompt function parameters etc.

At first sight, this is fairly trivial, but it took some effort to get right, so I felt it worth publishing.

The library is installable using pip and wont interfere with the Brython interpreter when the pages are uploaded. This is the recommended method, but if you prefer you can clone this directory to a directory OUTSIDE the script you are developing and add the directory to PYTHONPATH
eg

$ export PYTHONPATH=${PYTHONPATH}:${HOME}/mockbrython

then running a script containing brython calls will catch syntax errors without hitting unresolved Brython calls

$ python devel_script.py

The script can also be debugged using idle, our your IDE of choice. 

There is a simple example in the examples directory.
The script sample.py can be run from examples/index.html, or from the command line as

$ cd ${HOME}/mockbrython/examples ; python test.py

This includes a simulated event (a button click).

The script brythontest.py contains all the sample scripts in the section "Brython-specific built-in modules" from the documentation part of the Brython website and should run locally without errors and can be inpected with a debugger.

