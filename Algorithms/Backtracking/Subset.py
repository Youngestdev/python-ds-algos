import math

def subset(parent):
    output = []
    n = len(parent)

    def backtrack(idx, current): # [2,3] and [3,2]
        if len(current) == k:
            if len(current) > 1 and current[:] not in output and current[::-1] not in output:
                if math.gcd(current[0], current[len(current)-1]) > 1:
                    output.append(current[:])
        for i in range(idx, n):
            current.append(parent[i])
            backtrack(i+1, current)
            current.pop()
    for k in range(len(parent)+1):
        backtrack(0, [])
    return output


if __name__ == '__main__':
    print(subset([5, 2, 3, 2, 3, 3]))
    # print(smtn([5, 2, 3, 2, 3, 3]))