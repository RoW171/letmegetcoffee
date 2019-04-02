__author__ = "Robin 'r0w' Weiland"
__date__ = "2019-04-02"
__version__ = "0.0.1"

from random import randint
from letmegetcoffee import lmgc
lmgc.ON_EXCEPTION = lmgc.on_exception_beep


@lmgc.catch
def testing(number, message):
    print(message)
    while True: number / randint(0, number)


if __name__ == '__main__':
    testing(1000000, message='Hello World!!!')
