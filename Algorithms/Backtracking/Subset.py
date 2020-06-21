def subset(parent):
    output = []
    n = len(parent)
    # 1,2,3
    def backtrack(idx = 0, current=[]):
        if len(current) == k:
            output.append(current[:])
        for i in range(idx, n):
            current.append(parent[i])
            backtrack(i+1, current)
            current.pop()
    for k in range(len(parent)+1):
        backtrack(0, [])
    return output

print(subset([1,2,3]))