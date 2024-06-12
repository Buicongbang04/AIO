import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def elu(x, a=0.01):
    return np.where(x > 0, x, a * (np.exp(x) - 1))


def is_number(x):
    try:
        if type(x) is str:
            raise TypeError("x must be a number")

        activation_func = input("Enter the activation function: ")
        if activation_func not in ["sigmoid", "relu", "elu"]:
            raise TypeError(
                f'Activation function "{activation_func}" is not supported.')

        if activation_func == "sigmoid":
            return sigmoid(x)
        elif activation_func == "relu":
            return relu(x)
        elif activation_func == "elu":
            return elu(x)

    except Exception as e:
        print(e)
        return False

    return True
