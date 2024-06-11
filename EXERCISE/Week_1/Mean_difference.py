import math


def mean_difference(yi, yhat, n, p):
    sum = 0
    for i in range(n):
        sum += (yi**(1/n) - yhat**(1/n))**p
    sum = sum/n
    return sum
