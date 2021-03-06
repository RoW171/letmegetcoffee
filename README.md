# letmegetcoffee
A python module that provides functionality to notify you when something
goes wrong

# Usage

    from letmegetcoffee import lmgc  # or use wild import since it equals to lmgc only

error(s) to catch; defaults to (Exception,); not necessary to set

    lmgc.EXCEPTIONS = ValueError

what to do if an error occurred; necessary to set after import, since it
defaults to `print` and just silently prints the exception-object

    lmgc.ON_EXCEPTION = lmgc.on_exception_beep

# on_exception_ - functions

- ```on_exception_beep(e):```

     Beep in a while loop to notify if something goes wrong.
     **Remeber to turn your volume up**

- ```on_exception_mail(e):``` **[IN DEVELOPEMENT]**

    Send an email to notify if something goes wrong.

- ```on_exception_webpage(e):```  **[IN DEVELOPEMENT]**

    Host a webpage inside the local network to show the state of the
    running program.
    Seems unlikly though since hosting an http server (during the entire
    runtime, not only when an error occured) is a rather
    resource-expensive task

It is also possible to use your own function. Just note:

- the function has to take the excepion-object as an argument

    exception-object like in ```except Exception as e: pass```

- ```lmgc.ON_EXCEPTION = yourFunction``` has to be set before the
  decorator is used


# Example
```
from random import randint
from letmegetcoffee import lmgc
lmgc.ON_EXCEPTION = lmgc.on_exception_beep


@lmgc.catch
def testing(number, message):
    print(message)
    while True: number / randint(0, number)


if __name__ == '__main__':
    testing(1000000, message='Hello World!!!')  # args and kwargs work

```
