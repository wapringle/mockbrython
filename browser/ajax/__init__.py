from browser.html import _htmltype
Ajax=_htmltype

def get(url, blocking=False, headers={}, mode="text", encoding="utf-8", timeout=None, cache=False, data="", **callbacks):
    pass

def post(url, blocking=False, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=None, data="", **callbacks):
    pass

def file_upload(url, file, method="POST", field_name="filetosave", **callbacks):
    pass

