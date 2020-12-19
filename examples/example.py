from random import random
from retry_module.decorators import retry

@retry(Exception)
def f():
    x = random()

    if x < 0.7:
        raise Exception("Faulty code!")
    else:
        return "Success!"

print(f())