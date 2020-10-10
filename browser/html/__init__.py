
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

class _htmltype(dict):
    def __init__(self, *args, **kwargs):
        self.style = _htmltype1()
        self.args = args
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __le__(self, other):
        pass

    def __add__(self, other):
        """ Brython overloads the add operater to concatenate 2 brython objects
            We mock this by returning a _htmltype, 
            except where the other operand is an int when we return a zero
        """

        if type(other) == _htmltype:
            return self
        else:
            return 0

    def __radd__(self, other):
        """ and make symmetric """
        if type(other) == _htmltype:
            return self
        else:
            return 0

    def __sub__(self, other):
        return 0

    def __int__(self):
        return 0

    def __mul__(self, other):
        return 0

    def __truediv__(self, other):
        return 0

    def __getattr__(self, attr):
        return self

""" HTML4 tags """

A = _htmltype
ABBR = _htmltype
ACRONYM = _htmltype
ADDRESS = _htmltype
APPLET = _htmltype
AREA = _htmltype
B = _htmltype
BASE = _htmltype
BASEFONT = _htmltype
BDO = _htmltype
BIG = _htmltype
BLOCKQUOTE = _htmltype
BODY = _htmltype
BR = _htmltype
BUTTON = _htmltype
CAPTION = _htmltype
CENTER = _htmltype
CITE = _htmltype
CODE = _htmltype
COL = _htmltype
COLGROUP = _htmltype
DD = _htmltype
DEL = _htmltype
DFN = _htmltype
DIR = _htmltype
DIV = _htmltype
DL = _htmltype
DT = _htmltype
EM = _htmltype
FIELDSET = _htmltype
FONT = _htmltype
FORM = _htmltype
FRAME = _htmltype
FRAMESET = _htmltype
H1 = _htmltype
H2 = _htmltype
H3 = _htmltype
H4 = _htmltype
H5 = _htmltype
H6 = _htmltype
HEAD = _htmltype
HR = _htmltype
HTML = _htmltype
I = _htmltype
IFRAME = _htmltype
IMG = _htmltype
INPUT = _htmltype
INS = _htmltype
ISINDEX = _htmltype
KBD = _htmltype
LABEL = _htmltype
LEGEND = _htmltype
LI = _htmltype
LINK = _htmltype
MAP = _htmltype
MENU = _htmltype
META = _htmltype
NOFRAMES = _htmltype
NOSCRIPT = _htmltype
OBJECT = _htmltype
OL = _htmltype
OPTGROUP = _htmltype
OPTION = _htmltype
P = _htmltype
PARAM = _htmltype
PRE = _htmltype
Q = _htmltype
S = _htmltype
SAMP = _htmltype
SCRIPT = _htmltype
SELECT = _htmltype
SMALL = _htmltype
SPAN = _htmltype
STRIKE = _htmltype
STRONG = _htmltype
STYLE = _htmltype
SUB = _htmltype
SUP = _htmltype
SVG = _htmltype
TABLE = _htmltype
TBODY = _htmltype
TD = _htmltype
TEXTAREA = _htmltype
TFOOT = _htmltype
TH = _htmltype
THEAD = _htmltype
TITLE = _htmltype
TR = _htmltype
TT = _htmltype
U = _htmltype
UL = _htmltype
VAR = _htmltype

""" HTML5 tags """
ARTICLE=_htmltype
ASIDE=_htmltype
AUDIO=_htmltype
BDI=_htmltype
CANVAS=_htmltype
COMMAND=_htmltype
DATA=_htmltype
DATALIST=_htmltype
EMBED=_htmltype
FIGCAPTION=_htmltype
FIGURE=_htmltype
FOOTER=_htmltype
HEADER=_htmltype
KEYGEN=_htmltype
MAIN=_htmltype
MARK=_htmltype
MATH=_htmltype
METER=_htmltype
NAV=_htmltype
OUTPUT=_htmltype
PROGRESS=_htmltype
RB=_htmltype
RP=_htmltype
RT=_htmltype
RTC=_htmltype
RUBY=_htmltype
SECTION=_htmltype
SOURCE=_htmltype
SUMMARY=_htmltype
TEMPLATE=_htmltype
TIME=_htmltype
TRACK=_htmltype
VIDEO=_htmltype
WBR=_htmltype

""" HTML5.1 tags """

DETAILS=_htmltype
DIALOG=_htmltype
MENUITEM=_htmltype
PICTURE=_htmltype
SUMMARY=_htmltype


class _EV():
    """ This class can create dummy events """

    def __init__(self, id):
        self.currentTarget = _htmltype(id=id)
