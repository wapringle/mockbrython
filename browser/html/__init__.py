class _htmltype():
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
        for k,v in kwargs.items():
            setattr(self,k,v)
        pass


    def __call__(self,*args,**kwargs):
        return self

    def __le__(self,other):
        pass

    def __add__(self,other):
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

""" Create dummy entries for html calls"""
for _a in "A, ABBR, ACRONYM, ADDRESS, APPLET, AREA, B, BASE, BASEFONT, BDO, BIG, BLOCKQUOTE, BODY, BR, BUTTON, CANVAS, CAPTION, CENTER, CITE, CODE, COL, COLGROUP, DD, DEL, DFN, DIR, DIV, DL, DT, EM, FIELDSET, FONT, FORM, FRAME, FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML, I, IFRAME, IMG, INPUT, INS, ISINDEX, KBD, LABEL, LEGEND, LI, LINK, MAP, MENU, META, NOFRAMES, NOSCRIPT, OBJECT, OL, OPTGROUP, OPTION, P, PARAM, PRE, Q, S, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, STRONG, STYLE, SUB, SUP, SVG, TABLE, TBODY, TD, TEXTAREA, TFOOT, TH, THEAD, TITLE, TR, TT, U, UL, VAR".split(", "):
        exec('%s=_htmltype' % _a )
del _a    

class _EV():
    """ This class can create dummy events """
    def __init__(self,id):
        self.currentTarget=_htmltype(id=id)