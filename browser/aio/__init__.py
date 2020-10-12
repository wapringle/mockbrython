from browser.html import _htmltype
async def ajax(method, url, format="text", headers=None, data=None, cache=False):
    return _htmltype()

async def get(url, format="text", headers=None, data=None, cache=False):
    return _htmltype()
async def post(url, format="text", headers=None, data=None):
    return _htmltype()
    
_event_return=_htmltype()
""" If you want to force """
async def event(element, name):
    return _event_return

#evt = await aio.event(element, "click") suspends execution of an asynchronous function until the user clicks on the specified element. The return value is an instance of the DOMEvent class (cf. section events)
def sleep(seconds):
    pass

import asyncio
def run(coroutine):
    asyncio.run(coroutine)
    pass
    
