string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*'
from itertools import combinations_with_replacement as c
def gen_combinations():
    i = 0
    while True:
        x = list(c(string,3))
        y = x[i]
        i += 1
        yield y
trial = gen_combinations()
while True:
    print(next(trial))
