from browser import document, html, alert
from browser.html import *

""" When button is pressed, ok BTN  is displayed on console log."""
def show(ev):
    id=ev.currentTarget.id
    print('ok',id)

def load():
    btn=BUTTON("Press me", id="BTN")
    document <= DIV(btn)
    

    btn.bind("click", show)    
    
