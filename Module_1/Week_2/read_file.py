def word_count(url: str):
    result = dict()
    with open(url, 'r') as file:
        data = file.read()
        for word in data.split():
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result


if __name__ == '__main__':
    print(word_count('D:\Study\AI-Book\AIO\EXERCISE\Week_2\data\P1_data.txt'))
