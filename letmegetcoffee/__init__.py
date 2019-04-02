#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__credits__ = ["Robin Weiland", ]
__copyright__ = "Copyright 2019, Robin Weiland"

__date__ = "2019-04-01"
__version__ = "0.1.0"
__license__ = "MIT"

__status__ = "In Development"
__maintainer__ = "Robin Weiland"

__all__ = ['lmgc']

# imports:
from warnings import warn
from platform import system
from time import sleep
# 'from winsound import Beep' on line 43, since it is platform specific
from _thread import start_new_thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


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

        message = RESPONSE.format(color='red' if lmgc.ERROR_STATE else 'green',
                                  message='Everything seems alright' if lmgc.ERROR_MESSAGE is str() else lmgc.ERROR_MESSAGE)

        self.wfile.write(bytes(message, 'utf-8'))
        return


def startserver(address='localhost', port=12345):
    server = TCPServer((address, port), HTTPHandler)
    server.serve_forever()
    return server


class lmgc:
    EXCEPTIONS = (Exception,)
    ON_EXCEPTION = print
    # noinspection PyArgumentList
    ERROR_STATE = bool()
    ERROR_MESSAGE = str()

    @staticmethod
    def catch(func):
        if lmgc.ON_EXCEPTION is print: warn('lmgc.ON_EXCEPTION is not specified; defaults to print')
        if lmgc.ON_EXCEPTION is lmgc.on_exception_webpage: start_new_thread(startserver, ())

        def wrapper():
            try: func()
            except lmgc.EXCEPTIONS as e: lmgc.ON_EXCEPTION(e)
        return wrapper

    @staticmethod
    def on_exception_beep(e):
        lmgc.ERROR = True
        name = e.__class__.__name__
        line = e.__traceback__.tb_lineno
        file = e.__traceback__.tb_frame.f_code.co_filename
        print('{} at line {} in file \'{}\''.format(name, line, file))
        lmgc.ERROR_MESSAGE = '{} at line {} in file \'{}\''.format(name, line, file)
        if system() == 'Windows':
            from winsound import Beep
            while True:
                Beep(1000, 1000)
                sleep(0.5)
        elif system() in ('Linux', 'Darwin',):
            while True:
                print('\a', sep='')
                sleep(0.5)

    @staticmethod
    def on_exception_webpage(e):
        lmgc.ERROR = True
        name = e.__class__.__name__
        line = e.__traceback__.tb_lineno
        file = e.__traceback__.tb_frame.f_code.co_filename
        print('{} at line {} in file \'{}\''.format(name, line, file))
        lmgc.ERROR_MESSAGE = '{} at line {} in file \'{}\''.format(name, line, file)


lmgc.ON_EXCEPTION = lmgc.on_exception_webpage


@lmgc.catch
def testing():
    from random import randint
    from time import sleep
    number = 1000000
    # while True: number / randint(0, number)
    sleep(10)
    print(30 / 0)


if __name__ == '__main__':
    testing()
