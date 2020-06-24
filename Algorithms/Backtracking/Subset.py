def subset(parent):
    output = []
    n = len(parent)

    def backtrack(idx, current):
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