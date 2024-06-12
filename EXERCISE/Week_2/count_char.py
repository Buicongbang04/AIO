import pandas as pd


def count_char(string: str) -> dict:
    char_dict = {}
    for ch in string:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict


if __name__ == "__main__":
    string = "Hello, World!"
    print(count_char(string))
    string = "Python is fun!"
    print(count_char(string))
    string = "Happiness"
    print(count_char(string))
