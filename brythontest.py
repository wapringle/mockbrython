from browser import html
evt=html._EV(99) # used to exercise event handlers


""" Test mockbrython functionality. See how we can develop and test Brython scripts.
    The following scripts are lifted from the section "Brython-specific built-in modules" 
    from the documentation part of the Brython website. 
    I have added a few calls to exercise event handlers. Otherwise the are unchanged. 
    They should run with all Brython-specific parts dummied out.
"""

""" browser.aio """

from browser import alert, document, html, aio

async def main():
    input = html.INPUT()
    document <= input
    while True:
        ev = await aio.event(input, "blur")
        try:
            v = int(ev.target.value)
            input.remove()
            alert(f"Value: {v}")
            break
        except ValueError:
            input.value = ""

aio.run(main())

from browser import document, html, aio

async def main():
    # Text file
    req = await aio.ajax("GET", "test.html")
    print(len(req.data))
    # Binary file
    req = await aio.get("memo.pdf", format="binary")
    print(len(req.data))
    # Read binary file as dataURL
    req = await aio.get("eraser.png", format="dataURL")
    # display the image in an IMG tag
    document <= html.IMG(src=req.data)

aio.run(main())

""" browser.ajax """

from browser import document, ajax

def on_complete(req):
    if req.status == 200 or req.status == 0:
        document["result"].html = req.text
    else:
        document["result"].html = "error " + req.text

url=""
req = ajax.Ajax()
req.bind('complete', on_complete)
# send a POST request to the url
req.open('POST', url, True)
req.set_header('content-type', 'application/x-www-form-urlencoded')
# send data as a dictionary
req.send({'x': 0, 'y': 1})

from browser import document, ajax

def on_complete(req):
    if req.status == 200:
        document["result"].html = req.text
    else:
        document["result"].html = "error " + req.text

ajax.post(url,
          data={'x': 0, 'y': 1},
          oncomplete=on_complete)

from browser import ajax

def read(f):
    data = f.read()
    assert isinstance(data, bytes)

req = ajax.get("tests.zip", mode="binary",
    oncomplete=read)


from browser import ajax, bind, document

def upload_ok(req):
    print("all right")

@bind("#upload", "click")
def uploadfiles(event):
    for f in document["choosefiles"].files:
        ajax.file_upload("/cgi-bin/savefile.py", f,
            oncomplete=upload_ok)

uploadfiles(evt)  ## added
""" browser.html """        
# First of all, the import of some libraries
from browser import document
from browser import html

# All the elements will be inserted in the div with the "container" id
container = document['container']

# We create a new div element
newdiv = html.DIV(id = "new-div")
# Now we add some style
newdiv.style = {"padding": "5px",
               "backgroundColor": "#ADD8E6"}

# Now, lets add a table with a column with numbers and a
# column with a word on each cell
text = "Brython is really cool"
textlist = text.split()
table = html.TABLE()
for i, word in enumerate(textlist):
    table <= html.TR(html.TD(i + 1) +
                     html.TD(word))
# Now we add some style to the table
table.style = {"padding": "5px",
               "backgroundColor": "#aaaaaa",
               "width": "100%"}
# Now we add the table to the new div previously created
newdiv <= table + html.BR()

# a form? why not?
form = html.FORM()
input1 = html.INPUT(type="text", name="firstname", value="First name")
input2 = html.INPUT(type="text", name="lastname", value="Last name")
input3 = html.BUTTON("Button with no action!")
form <= input1 + html.BR() + input2 + html.BR() + input3

newdiv <= form + html.BR()

# Finally, we will add something more 'HTML5istic', a canvas with
# a color gradient in the newdiv previously created and below the form
canvas = html.CANVAS(width = 300, height = 300)
canvas.style = {"width": "100%"}
ctx = canvas.getContext('2d')
ctx.rect(0, 0, 300, 300)
grd = ctx.createRadialGradient(150, 150, 10, 150, 150, 150)
grd.addColorStop(0, '#8ED6FF')
grd.addColorStop(1, '#004CB3')
ctx.fillStyle = grd
ctx.fill()

newdiv <= canvas

# And finally we append the newdiv element
# to the parent, in this case the div with the "container" id
container <= newdiv
        
""" browser.local_storage """
        
from browser.local_storage import storage
storage['foo'] = 'bar'
print(storage['foo']) 


del storage['foo']
try:
    print(storage['foo']) # raises KeyError ## added exception handler
except KeyError as e:
    print("KeyError expected")
    
""" browser.markdown """

from browser import document as doc
from browser import markdown

src="" # instead of open(url).read()
mk, scripts = markdown.mark(src)
doc['zone'].html = mk
for script in scripts:
    exec(script,globals())

""" browser.ObjectStorage """

from browser.session_storage import storage
from browser.object_storage import ObjectStorage

object_storage = ObjectStorage(storage)
object_storage[['do', 're', 'me']] = {"tune": "in tune"}

# to update the value, need to copy out first
tmp = object_storage[['do', 're', 'me']]
tmp.update({"duration": "one hour"})
object_storage[['do', 're', 'me']] = tmp

""" browser.session_storage """

from browser.session_storage import storage
storage['foo'] = 'bar'
print(storage['foo'])

""" browser.svg """

from browser import document, svg

line = svg.line(x1="40",y1="50", x2="40", y2="150",
                stroke="brown",stroke_width="2")

panel = document['panel3']
panel <= line


from browser import document, svg

star = svg.polygon(fill="red", stroke="blue", stroke_width="10",
                   points=""" 75,38  90,80  135,80  98,107
                             111,150 75,125  38,150 51,107
                              15,80  60,80""")

panel = document['panel4']
panel <= star


from browser import document, svg, timer

rect = svg.rect(x=10, y=10, width=100, height=100)

def move_rect():
    # the attributes of the SVG element are strings, they must be explicitely
    # converted into integers
    rect.attrs["y"] = int(rect.attrs["y"]) + 1
    
    # ends animation when the rectangle reaches its target
    if int(rect.attrs["y"] ) > 50:
        timer.clear_interval(loop)

panel = document['panel5']
panel <= rect

# initialise the animation loop
loop = timer.set_interval(move_rect, 30)

""" browser.timer """

from browser import document as doc
from browser import timer

def change_color():
    doc['first-text'].style.color = "blue"

def press_button(ev):
    timer.set_timeout(change_color, 3000)

doc['first-button'].bind('click', press_button)


from browser import document, timer

idtimer = 1

def change_color_two():
    document['ct-text2'].style.color = "blue"

def press_button_two(ev):
    global idtimer
    idtimer = timer.set_timeout(change_color_two, 3000)
    
def stop_button(ev):
    timer.clear_timeout(idtimer)

document['ct-start'].bind('click', press_button_two)
document['ct-stop'].bind('click', stop_button)
press_button_two(html._EV(99)) ## added


import time
from browser import document as doc
from browser import timer

_timer = None
counter = 0

def show():
    doc['_timer'].text = '%.2f' %(time.time()-counter)

def start_timer(ev):
    global _timer,counter
    if _timer is None:
        counter = time.time()
        _timer = timer.set_interval(show,10)
        doc['start'].text = 'Hold'
    elif _timer == 'hold': # restart
        # restart timer
        counter = time.time()-float(doc['_timer'].text)
        _timer = timer.set_interval(show,10)
        doc['start'].text = 'Hold'
    else: # hold
        timer.clear_interval(_timer)
        _timer = 'hold'
        doc['start'].text = 'Restart'

def stop_timer(ev):
    global _timer
    timer.clear_interval(_timer)
    _timer = None
    t = 0
    doc['_timer'].text = '%.2f' %0
    doc['start'].text = 'Start'

doc['start'].bind('click', start_timer)
doc['stop'].bind('click', stop_timer)
start_timer(evt)
stop_timer(evt)


from browser.timer import request_animation_frame as raf
from browser.timer import cancel_animation_frame as caf
from browser import document as doc
from browser import window as win
from time import time
from browser.html import CANVAS, BUTTON
import math

ctx = doc['raf-canvas'].getContext( '2d' ) 

toggle = True

def draw():
    t = time() * 3
    x = math.sin(t) * 96 + 128
    y = math.cos(t * 0.9) * 96 + 128
    global toggle
    if toggle:
        toggle = False
    else:
        toggle = True
    ctx.fillStyle = 'rgb(200,200,20)' if toggle else 'rgb(20,20,200)'
    ctx.beginPath()
    ctx.arc( x, y, 6, 0, math.pi * 2, True)
    ctx.closePath()
    ctx.fill()

def animate(i):
    global id
    id = raf(animate)
    draw()

def stop(i):
    global id
    print(id)
    caf(id)

doc['btn-animate'].bind('click', animate)
doc['btn-stop'].bind('click', stop)

## added
animate(evt)
draw() # added
stop(evt)

""" browser.Template """


from browser import document
from browser.template import Template

Template(document["team"]).render(name="Liverpool FC")

""" browser.webcomponent """

from browser import webcomponent

class BoldItalic:

    def __init__(self):
        # Create a shadow root
        shadow = self.attachShadow({'mode': 'open'})

        # Insert the value of attribute "data-val" in bold italic
        # in the shadow root
        shadow <= html.B(html.I(self.attrs['data-val']))

# Tell the browser to manage <bold-italic> tags with the class BoldItalic
webcomponent.define("bold-italic", BoldItalic)

import browser.webcomponent

class BoldItalic:

    def __init__(self):
        # Create a shadow root
        shadow = self.attachShadow({'mode': 'open'})

        # Insert the value of attribute "data-val" in bold italic
        # in the shadow root
        shadow <= html.B(html.I(self.attrs['data-val']))

    def connectedCallback(self):
        print("connected callback", self)

webcomponent.define("bold-italic", BoldItalic)

observed_tag = html.maketag("observed-element")

class Observed:

    def observedAttributes(self):
        return ["data"]

    def attributeChangedCallback(self, name, old, new, ns):
        print(f"attribute {name} changed from {old} to {new}")

webcomponent.define("observed-element", Observed)

elt = observed_tag()
document <= elt
elt.attrs["data"] = "info"

""" browser.websocket """

from browser import bind, document, websocket
from browser.widgets.dialog import InfoDialog

def on_open(evt):
    document['sendbtn'].disabled = False
    document['closebtn'].disabled = False
    document['openbtn'].disabled = True
    InfoDialog("websocket", f"Connection open")    

def on_message(evt):
    # message received from server
    InfoDialog("websocket", f"Message received : {evt.data}")

def on_close(evt):
    # websocket is closed
    InfoDialog("websocket", "Connection is closed")
    document['openbtn'].disabled = False
    document['closebtn'].disabled = True
    document['sendbtn'].disabled = True

ws = None

@bind('#openbtn', 'click')
def _open(ev):
    if not websocket.supported:
        InfoDialog("websocket", "WebSocket is not supported by your browser")
        return
    global ws
    # open a web socket
    ws = websocket.WebSocket("wss://echo.websocket.org")
    # bind functions to web socket events
    ws.bind('open',on_open)
    ws.bind('message',on_message)
    ws.bind('close',on_close)

@bind('#sendbtn', 'click')
def send(ev):
    data = document["data"].value
    if data:
        ws.send(data)

@bind('#closebtn', 'click')
def close_connection(ev):
    ws.close()
    document['openbtn'].disabled = False

## added calls to exercise callbacks
    
_open(evt)
send(evt)
close_connection(evt)

on_open(evt)
on_message(evt)
on_close(evt)


""" browser.worker """


"""Main script."""

from browser import bind, document, worker

result = document.select_one('.result')
inputs = document.select("input")

# Create a web worker, identified by a script id in this page.
myWorker = worker.Worker("worker")

@bind(inputs, "change")
def change(evt):
    """Called when the value in one of the input fields changes."""
    # Send a message (here a list of values) to the worker
    myWorker.send([x.value for x in inputs])

@bind(myWorker, "message")
def onmessage(e):
    """Handles the messages sent by the worker."""
    result.text = e.data

# Code of the worker script:
"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self

@bind(self, "message")
def message(evt):
    """Handle a message sent by the main script.
    evt.data is the message body.
    """
    try:
        result = int(evt.data[0]) * int(evt.data[1])
        workerResult = f'Result: {result}'
        # Send a message to the main script.
        # In the main script, it will be handled by the function bound to
        # the event "message" for the worker.
        self.send(workerResult)
    except ValueError:
        self.send('Please write two numbers')

## exercise event handlers
for f in change, onmessage,message:
    f(evt)
    
    

print("done")        