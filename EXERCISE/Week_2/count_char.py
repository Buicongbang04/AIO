import pandas as pd


def countChar(string: str) -> dict:
    char_dict = {}
    for ch in string:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict


if __name__ == "__main__":
    string = "Hello, World!"
    print(countChar(string))
    string = "Python is fun!"
    print(countChar(string))
    string = "Happiness"
    print(countChar(string))
