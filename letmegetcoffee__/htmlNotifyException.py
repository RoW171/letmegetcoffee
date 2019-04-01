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
from ssl import wrap_socket
from socketserver import TCPServer


RESPONSE = """
<html>
    <head>
        <title>Test</title>
    </head>
    <script type="text/javascript">
        function notifyMe() {
            if (!("Notification" in window)) {
                alert("This browser does not support system notifications");
                }
            else if (Notification.permission === "granted") {
                var notification = new Notification("Hi there!");
                }
            else if (Notification.permission !== 'denied') {
                Notification.requestPermission(function (permission) {
                    if (permission === "granted") {
                        var notification = new Notification("Hi there!");
                            }
                        });
                    }
                }
        function note(){
            var notification = new Notification("this is a test");

            }
    </script>
    <body>
        this is a new test
        <script type="text/javascript">
            notifyMe();
            note();
        </script>
        <button type="button" onclick="var notification = new Notification("Hi there!")">Test Me!</button>
    </body>
</html>
"""


class HTTPHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print('-' * 10)
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = RESPONSE

        self.wfile.write(bytes(message, 'utf-8'))
        return


class HTMLNotifyException(BaseException): pass


def serve(address=''):
    server = TCPServer((address, 12345), HTTPHandler)
    # server.socket = wrap_socket(server.socket)
    server.serve_forever()


if __name__ == '__main__': serve()
else: pass
