import numpy as np


def check_list(num_list: list, k: int):
    for i in range(len(num_list) - k + 1):
        max_num = max(num_list[i:i+k])
        print(f"max {max_num}")


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    check_list(num_list, k)
