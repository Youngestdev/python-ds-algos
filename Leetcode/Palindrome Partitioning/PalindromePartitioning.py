def palindromePartitioning(string):
    result = []

    def backtrack(word, current):
        if len(word) == 0:
            result.append(current[:])
            return
        for i in range(1, len(word)+1):
            if word[:i] == word[:i][::-1]:
                backtrack(word[i:], current + [word[:i]])

    backtrack(string, [])
    return result


print(palindromePartitioning("abdulazeez"))
# [['a', 'b', 'd', 'u', 'l', 'a', 'z', 'e', 'e', 'z'], ['a', 'b', 'd', 'u', 'l', 'a', 'z', 'ee', 'z'], ['a', 'b', 'd', 'u', 'l', 'a', 'zeez']]