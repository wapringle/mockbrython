from browser import _mockbrython

supported = True

class _Websocket():
    def bind(self, evt, function):
        pass

    def send(self, data):
        pass

    def close(self):
        pass


def WebSocket(host):
    return _Websocket()


