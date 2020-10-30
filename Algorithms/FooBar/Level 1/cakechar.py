def solution(s):
    count = []
    for i in range(len(s)):
        terror = s[:i]*s.count(s[:i])
        print(terror)
        if s[:i]*s.count(s[:i]) == s:
            count.append(s.count(s[:i]))

    return max(count)

if __name__ == '__main__':
    print(solution("abcabcabcabc"))
    print(solution("abccbaabccba"))