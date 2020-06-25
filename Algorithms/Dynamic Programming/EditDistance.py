def editDistance(first, second):
    # Very very very crazy gamble here - because I don't know what's happening here sha.
    # By the end of this entire book, I'll be an expert, insha Allah

    """

    :param first: First word
    :param second: second word
    :return:

    There are three operations carried out:
    1. Insertion: fn(i, j-1) + 1
    2. Deletion: fn(i-1, j) + 1
    3. Substitution: fn(i-1, j-1) if characters of indices i & j are equal, else fn(i-1, j-1) + 1
    """

    m = len(first)
    n = len(second)
    edit = [[0]*(n+1) for _ in range(len(first) + 1)]
    for i in range(1, m+1):
        edit[i][0] = edit[i-1][0] + 1
    # print(edit)
    for i in range(1, n+1):
        edit[0][i] = edit[0][i-1]+1
    # print(edit)
    for i in range(1, m+1):
        for j in range(1, n+1):
            edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1, edit[i-1][j-1] + (0 if first[i-1] == second[j-1] else 1))
    # print(edit)
    return edit[-1][-1]

print(editDistance("ALGORITHM", "ALTRUISTIC"))