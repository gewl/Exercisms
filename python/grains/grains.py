import math

def on_square(num):
    return 2 ** (num-1)

def total_after(num):
    if (num == 0):
        return 0
    else:
        return on_square(num) + total_after(num-1)
