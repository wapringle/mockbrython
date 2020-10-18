
from browser import _mockbrython


""" HTML4 tags """

A = _mockbrython
ABBR = _mockbrython
ACRONYM = _mockbrython
ADDRESS = _mockbrython
APPLET = _mockbrython
AREA = _mockbrython
B = _mockbrython
BASE = _mockbrython
BASEFONT = _mockbrython
BDO = _mockbrython
BIG = _mockbrython
BLOCKQUOTE = _mockbrython
BODY = _mockbrython
BR = _mockbrython
BUTTON = _mockbrython
CAPTION = _mockbrython
CENTER = _mockbrython
CITE = _mockbrython
CODE = _mockbrython
COL = _mockbrython
COLGROUP = _mockbrython
DD = _mockbrython
DEL = _mockbrython
DFN = _mockbrython
DIR = _mockbrython
DIV = _mockbrython
DL = _mockbrython
DT = _mockbrython
EM = _mockbrython
FIELDSET = _mockbrython
FONT = _mockbrython
FORM = _mockbrython
FRAME = _mockbrython
FRAMESET = _mockbrython
H1 = _mockbrython
H2 = _mockbrython
H3 = _mockbrython
H4 = _mockbrython
H5 = _mockbrython
H6 = _mockbrython
HEAD = _mockbrython
HR = _mockbrython
HTML = _mockbrython
I = _mockbrython
IFRAME = _mockbrython
IMG = _mockbrython
INPUT = _mockbrython
INS = _mockbrython
ISINDEX = _mockbrython
KBD = _mockbrython
LABEL = _mockbrython
LEGEND = _mockbrython
LI = _mockbrython
LINK = _mockbrython
MAP = _mockbrython
MENU = _mockbrython
META = _mockbrython
NOFRAMES = _mockbrython
NOSCRIPT = _mockbrython
OBJECT = _mockbrython
OL = _mockbrython
OPTGROUP = _mockbrython
OPTION = _mockbrython
P = _mockbrython
PARAM = _mockbrython
PRE = _mockbrython
Q = _mockbrython
S = _mockbrython
SAMP = _mockbrython
SCRIPT = _mockbrython
SELECT = _mockbrython
SMALL = _mockbrython
SPAN = _mockbrython
STRIKE = _mockbrython
STRONG = _mockbrython
STYLE = _mockbrython
SUB = _mockbrython
SUP = _mockbrython
SVG = _mockbrython
TABLE = _mockbrython
TBODY = _mockbrython
TD = _mockbrython
TEXTAREA = _mockbrython
TFOOT = _mockbrython
TH = _mockbrython
THEAD = _mockbrython
TITLE = _mockbrython
TR = _mockbrython
TT = _mockbrython
U = _mockbrython
UL = _mockbrython
VAR = _mockbrython

""" HTML5 tags """
ARTICLE = _mockbrython
ASIDE = _mockbrython
AUDIO = _mockbrython
BDI = _mockbrython
CANVAS = _mockbrython
COMMAND = _mockbrython
DATA = _mockbrython
DATALIST = _mockbrython
EMBED = _mockbrython
FIGCAPTION = _mockbrython
FIGURE = _mockbrython
FOOTER = _mockbrython
HEADER = _mockbrython
KEYGEN = _mockbrython
MAIN = _mockbrython
MARK = _mockbrython
MATH = _mockbrython
METER = _mockbrython
NAV = _mockbrython
OUTPUT = _mockbrython
PROGRESS = _mockbrython
RB = _mockbrython
RP = _mockbrython
RT = _mockbrython
RTC = _mockbrython
RUBY = _mockbrython
SECTION = _mockbrython
SOURCE = _mockbrython
SUMMARY = _mockbrython
TEMPLATE = _mockbrython
TIME = _mockbrython
TRACK = _mockbrython
VIDEO = _mockbrython
WBR = _mockbrython

""" HTML5.1 tags """

DETAILS = _mockbrython
DIALOG = _mockbrython
MENUITEM = _mockbrython
PICTURE = _mockbrython
SUMMARY = _mockbrython


def maketag(name):
    return _mockbrython


def attribute_mapper(attr):
    return _mockbrython


class _EV(_mockbrython):
    """ This class can create dummy events """

    def __init__(self, id):
        self.currentTarget = _mockbrython(id=id)
