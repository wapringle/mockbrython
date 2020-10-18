from browser import _mockbrython


def InfoDialog(title, message, *, top=None, left=None, default_css=True, remove_after=None, ok=False):
    pass


def EntryDialog(title, message=None, *, top=None, left=None, default_css=True, ok=True):
    return _mockbrython()


def Dialog(title, *, top=None, left=None, default_css=True, ok_cancel=False):
    return _mockbrython()


