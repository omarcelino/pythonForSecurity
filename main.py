#!/usr/bin/python3
from datetime import datetime
from time import sleep


def logger(func):
    def wrappper(*args, **kwargs):
        print("Execution started at {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        result = func(*args, **kwargs)
        print("Execution finished at {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        return result

    return wrappper


@logger
def add(a, b):
    sleep(3)
    return a + b


print(add(5, 4))


