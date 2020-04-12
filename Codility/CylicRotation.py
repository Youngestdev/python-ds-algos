def solution(A, K):
    # write your code in Python 3.6
    ans = dict()
    if len(A) == K:
        return A

    for i in range(K):
        first_var = A.pop(-1)
        A.insert(0, first_var)
        ans[i] = A
    return ans[max(ans)]


x = [3,8,9,7,6]
y = [1,2,3,4]

print(solution(x, 3))
