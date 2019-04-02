#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__credits__ = ["Robin Weiland", ]
__copyright__ = "Copyright 2019, Robin Weiland"

__date__ = "2019-02-03"
__version__ = "0.1.0"
__license__ = "MIT"

__status__ = "In Development"
__maintainer__ = "Robin Weiland"

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from random import choice


RESPONSE = """
<html>
    <head> <title>LetMeGetCoffee</title></head>
    <body>
    <blockquote style="width: 90%; color: {color}; background-color: lightyellow; border: 5px solid {color};
    border-radius: 1em 1em 1em 1em; margin: 20px auto; padding: 2em; font-size: 2.5em; text-align: center;">
    <p>{message}</p></blockquote>
    </body>
</html>
"""


class HTTPHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = RESPONSE.format(color=choice(['red', 'green']),
                                  message=choice(['Everything seems fine',
                                                  'DivisionByZeroError at line 1 in file \'test.py\'']))

        self.wfile.write(bytes(message, 'utf-8'))
        return


class HTMLNotifyException(BaseException): pass


def serve(address=''):
    server = TCPServer((address, 12345), HTTPHandler)
    server.serve_forever()


if __name__ == '__main__': serve()
else: pass
