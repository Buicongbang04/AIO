import random
import numpy as np


def regression_loss_func(numb_samples):
    try:
        if not numb_samples.isnumeric():
            raise ValueError("Please enter a integer number")
        numb_samples = int(numb_samples)

        loss_name = input("Enter the loss function name: ").upper()
        if loss_name not in ['MAE', 'MSE', 'RMSE']:
            raise ValueError(f"{loss_name} is not supported")

        for i in range(numb_samples):
            pred = random.uniform(0, 10)
            target = random.uniform(0, 10)

            if loss_name == 'MAE':
                loss_value = mae(numb_samples, target, pred)
                display(loss_name, i, pred, target, loss_value)
            elif loss_name == 'MSE':
                loss_value = mse(numb_samples, target, pred)
                display(loss_name, i, pred, target, loss_value)
            elif loss_name == 'RMSE':
                loss_value = rmse(numb_samples, target, pred)
                display(loss_name, i, pred, target, loss_value)
    except Exception as e:
        print(e)


def display(loss_name, sample, pred, target, loss_value):
    print(f"Loss name: {loss_name}\nSample: {sample} | Prediction: {pred} | Target: {target} | Loss value: {loss_value}\n", end="\n")


def mae(n, yi, yhat):
    sum_ = 0
    for _ in range(0, n):
        sum_ += abs(yi - yhat)
    return sum_ / n


def mse(n, yi, yhat):
    sum_ = 0
    for _ in range(0, n):
        sum_ += (yi - yhat)**2
    return sum_ / n


def rmse(n, yi, yhat):
    sum_ = 0
    for _ in range(0, n):
        sum_ += (yi - yhat)**2
    return pow(sum_ / n, 0.5)
