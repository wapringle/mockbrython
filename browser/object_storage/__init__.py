from browser.html import _mockbrython


class ObjectStorage(dict):
    def __init__(self, s):
        pass

    def __getitem__(self, x):
        return _mockbrython

    def __setitem__(self, attr, value):
        pass


