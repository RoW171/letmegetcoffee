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
    """

    """

    EXCEPTIONS = (Exception,)
    ON_EXCEPTION = print

    @staticmethod
    def catch(func):
        """
        decorator for the function that should be monitored
        like this:

        @lmgc.catch
        def randomFunction(arg):
            ...

        :param func: the function; gets handled by the decorator
        :return: the wrapper; also part of the decorator
        """
        if lmgc.ON_EXCEPTION == print: warn('lmgc.ON_EXCEPTION is not specified; defaults to print')

        def wrapper(*args, **kwargs):
            try: func(*args, **kwargs)
            except lmgc.EXCEPTIONS as e: lmgc.ON_EXCEPTION(e)
        return wrapper

    @staticmethod
    def on_exception_beep(e):
        """
        beep when an error occurred, not to be called by the user, only set onto lmgc.ON_EXCEPTION
        :param e: Exception(child) object; passed by lmgc.catch
        :return: None
        """
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


lmgc.ON_EXCEPTION = lmgc.on_exception_beep


@lmgc.catch
def testing(number):
    from random import randint
    # number = 1000000
    counter = int()
    while True:
        counter += 1
        number / randint(0, number)
    print(counter)


if __name__ == '__main__':
    testing(20)
