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

    m = len(first) - 1
    n = len(second) - 1
    edit = [[0 for i in range(len(second))] for j in range(len(first))]

    for j in range(n+1):
        edit[0][j] = j

    for i in range(1, len(first)):
        edit[i][0] = i
        for j in range(1, len(second)):
            insertion = edit[i][j - 1] + 1
            deletion = edit[i - 1][j] + 1
            if first[i] == second[j]:
                repetition = edit[i - 1][j - 1]  # Same characters.
            else:
                repetition = edit[i - 1][j - 1] + 1 # Different characters
            edit[i][j] = min(insertion, deletion, repetition)

    return edit[m][n]


print(editDistance("ALGORITHM", "ALTRUISTIC")) # returns the correct answer
print(editDistance("FOOD", "MONEY")) # returns 3 instead of 4.
print(editDistance("azeez", "abdulazeez"))