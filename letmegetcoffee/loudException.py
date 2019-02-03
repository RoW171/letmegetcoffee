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


from platform import system
from traceback import format_exc
OS = system()

__doc__ = """Exception that makes an annoying beeping sound"""


def beep():
    """
    method to make the beep sound
    loops, so you will really notice th exception
    """
    from time import sleep
    if OS == 'Windows':
        from winsound import Beep
        while True:
            Beep(1000, 1000)
            sleep(0.5)
    elif OS == 'Linux' or OS == 'Darwin':
        while True:
            print('\a', sep='')
            sleep(0.5)


class LoudException(BaseException):
    __doc__ = __doc__

    def __init__(self, exc):
        """
        Exception that makes an annoying beeping sound
        :type exc: BaseException or child
        :param exc: exception, caught by 'except (Exception,) as e: raise LoudException(e)
        """
        super(LoudException, self).__init__()
        print(
            'Exception occured: {}'.format(type(exc).__name__),
            'description: {}'.format(exc),
            '-' * 8,
            'traceback:',
            format_exc(),
            sep='\n'
        )
        beep()


if __name__ == '__main__':
    print(LoudException.__init__.__doc__)
    # try: 1 / 0
    # except (ZeroDivisionError,) as e: raise LoudException(e)
