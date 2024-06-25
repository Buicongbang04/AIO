def levenshtein(string: str, target: str) -> int:
    if len(string) == 0:
        return len(target)
    if len(target) == 0:
        return len(string)
    if string[0] == target[0]:
        cost = 0
    else:
        cost = 1
    return min(
        levenshtein(string[1:], target) + 1,
        levenshtein(string, target[1:]) + 1,
        levenshtein(string[1:], target[1:]) + cost
    )


print(levenshtein("kitten", "sitting"))
print(levenshtein('yu', 'you'))
