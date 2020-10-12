from browser.html import _htmltype
Ajax=_htmltype

async def ajax(method, url, format="text", headers=None, data=None, cache=False):
    return _htmltype()
def get(url, blocking=False, headers={}, mode="text", encoding="utf-8", timeout=None, cache=False, data="", **callbacks):
    return _htmltype()

def post(url, blocking=False, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=None, data="", **callbacks):
    return _htmltype()

def file_upload(url, file, method="POST", field_name="filetosave", **callbacks):
    return _htmltype()

