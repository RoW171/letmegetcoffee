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


class lmgc:
    EXCEPTIONS = (Exception,)
    ON_EXCEPTION = print

    @staticmethod
    def catch(func):
        print(lmgc.ON_EXCEPTION)
        if lmgc.ON_EXCEPTION == print: warn('lmgc.ON_EXCEPTION is not specified; defaults to print')

        def wrapper():
            try: func()
            except lmgc.EXCEPTIONS as e: lmgc.ON_EXCEPTION(e)
        return wrapper

    @staticmethod
    def on_exception_beep(e):
        name = e.__class__.__name__
        line = e.__traceback__.tb_lineno
        file = e.__traceback__.tb_frame.f_code.co_filename
        print('{} at line {} in file \'{}\''.format(name, line, file))
        if system() == 'Windows':
            from winsound import Beep
            while True:
                Beep(1000, 1000)
                sleep(0.5)
        elif system() in ('Linux', 'Darwin',):
            while True:
                print('\a', sep='')
                sleep(0.5)


@lmgc.catch
def testing():
    from random import randint
    number = 1000000
    counter = int()
    while True:
        counter += 1
        number / randint(0, number)
    print(counter)


if __name__ == '__main__':
    testing()
