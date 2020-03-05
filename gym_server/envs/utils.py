"""Utility classes and mix-ins to make building environments easier."""
import socket


class ThreadedServerMixin:
    """Mix-in for a environment that uses socket-based communication."""

    def __init__(self, host: str, port: int, timeout: int = 60, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._timeout = timeout
        self._host = host
        self._port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.sock.connect((self._host, self._port))
        client, address = self.sock.accept()
        client.settimeout(self._timeout)

    def stop(self):
        self.sock.shutdown(socket.SHUT_RD)
        self.sock.close()
