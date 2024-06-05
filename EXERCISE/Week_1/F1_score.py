def f1_score(tp, fp, fn):
    try:
        if type(tp) != int:
            raise TypeError("tp must be an integer")
        elif type(fp) != int:
            raise TypeError("fp must be an integer")
        elif type(fn) != int:
            raise TypeError("fn must be an integer")

        if tp <= 0 or fp <= 0 or fn <= 0:
            raise ValueError("tp and fp and fn must be greater than 0")

        f1 = 2 * (precision(tp, fp) * recall(tp, fn)) / \
            (precision(tp, fp) + recall(tp, fn))

        return f1
    except Exception as e:
        print(e)


def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)
