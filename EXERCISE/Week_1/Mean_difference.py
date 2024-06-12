import math


def mean_difference(yi, yhat, n, p):
    sum_ = 0
    for _ in range(n):
        sum_ += (yi**(1/n) - yhat**(1/n))**p
    sum_ = sum_/n
    return sum_
