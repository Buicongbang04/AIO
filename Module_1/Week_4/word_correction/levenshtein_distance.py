def levenshtein_distance(s1: str, s2: str) -> int:
    distances = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    for t1 in range(len(s1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(s2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(s1) + 1):
        for t2 in range(1, len(s2) + 1):
            if s1[t1 - 1] == s2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if a <= b and c >= a:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    return distances[len(s1)][len(s2)]
