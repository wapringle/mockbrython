
class _htmltype2(dict):
    items = []
    
    def __missing__(self, attr):
        return _htmltype()

    def __getattr__(self, attr):
        return 0

    def __setattr__(self, attr, value):
        pass

class _htmltype():
    def __init__(self,*args,**kwargs):
        self.style=_htmltype2()
        self.args=args
        self.kwargs=kwargs
        for k,v in kwargs.items():
            setattr(self,k,v)
        pass


    def __call__(self,*args,**kwargs):
        return self

    def __le__(self,other):
        pass
    
    """ Brython overloads the add operater to concatenate 2 brython objects
        We mock this by returning a _htmltype, 
        excect where the other operand is an int when we return a zero
    """

    def __add__(self,other):
        
        if type(other)==_htmltype:
            return self
        else:
            return 0
    """ and make symmetric """
    def __radd__(self,other):
        if type(other)==_htmltype:
            return self
        else:
            return 0
    
    def __sub__(self,other):
        return 0
    
    def __mul__(self,other):
        return 0
    
    def __truediv__(self,other):
        return 0
    
    def __getattr__(self,attr):
        return self

""" Create dummy entries for html calls
for _a in "A, ABBR, ACRONYM, ADDRESS, APPLET, AREA, B, BASE, BASEFONT, BDO, BIG, BLOCKQUOTE, BODY, BR, BUTTON, CANVAS, CAPTION, CENTER, CITE, CODE, COL, COLGROUP, DD, DEL, DFN, DIR, DIV, DL, DT, EM, FIELDSET, FONT, FORM, FRAME, FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML, I, IFRAME, IMG, INPUT, INS, ISINDEX, KBD, LABEL, LEGEND, LI, LINK, MAP, MENU, META, NOFRAMES, NOSCRIPT, OBJECT, OL, OPTGROUP, OPTION, P, PARAM, PRE, Q, S, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, STRONG, STYLE, SUB, SUP, SVG, TABLE, TBODY, TD, TEXTAREA, TFOOT, TH, THEAD, TITLE, TR, TT, U, UL, VAR".split(", "):
        exec('%s=_htmltype' % _a )
del _a    
"""
A=_htmltype
ABBR=_htmltype
ACRONYM=_htmltype
ADDRESS=_htmltype
APPLET=_htmltype
AREA=_htmltype
B=_htmltype
BASE=_htmltype
BASEFONT=_htmltype
BDO=_htmltype
BIG=_htmltype
BLOCKQUOTE=_htmltype
BODY=_htmltype
BR=_htmltype
BUTTON=_htmltype
CANVAS=_htmltype
CAPTION=_htmltype
CENTER=_htmltype
CITE=_htmltype
CODE=_htmltype
COL=_htmltype
COLGROUP=_htmltype
DD=_htmltype
DEL=_htmltype
DFN=_htmltype
DIR=_htmltype
DIV=_htmltype
DL=_htmltype
DT=_htmltype
EM=_htmltype
FIELDSET=_htmltype
FONT=_htmltype
FORM=_htmltype
FRAME=_htmltype
FRAMESET=_htmltype
H1=_htmltype
H2=_htmltype
H3=_htmltype
H4=_htmltype
H5=_htmltype
H6=_htmltype
HEAD=_htmltype
HR=_htmltype
HTML=_htmltype
I=_htmltype
IFRAME=_htmltype
IMG=_htmltype
INPUT=_htmltype
INS=_htmltype
ISINDEX=_htmltype
KBD=_htmltype
LABEL=_htmltype
LEGEND=_htmltype
LI=_htmltype
LINK=_htmltype
MAP=_htmltype
MENU=_htmltype
META=_htmltype
NOFRAMES=_htmltype
NOSCRIPT=_htmltype
OBJECT=_htmltype
OL=_htmltype
OPTGROUP=_htmltype
OPTION=_htmltype
P=_htmltype
PARAM=_htmltype
PRE=_htmltype
Q=_htmltype
S=_htmltype
SAMP=_htmltype
SCRIPT=_htmltype
SELECT=_htmltype
SMALL=_htmltype
SPAN=_htmltype
STRIKE=_htmltype
STRONG=_htmltype
STYLE=_htmltype
SUB=_htmltype
SUP=_htmltype
SVG=_htmltype
TABLE=_htmltype
TBODY=_htmltype
TD=_htmltype
TEXTAREA=_htmltype
TFOOT=_htmltype
TH=_htmltype
THEAD=_htmltype
TITLE=_htmltype
TR=_htmltype
TT=_htmltype
U=_htmltype
UL=_htmltype
VAR=_htmltype

class _EV():
    """ This class can create dummy events """
    def __init__(self,id):
        self.currentTarget=_htmltype(id=id)