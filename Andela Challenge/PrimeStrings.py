# Backtracking solution but isn't efficient for large inputs...

# Helper function `isPrime(number)` helps to check if it's prime or not.

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeStrings(string):
    output = []
    n = len(string)
    def backtrack(substr, current):
        if len(substr) == 0:
            output.append(current.copy())
            return
        for i in range(1, len(substr)+1):
            if isPrime(int(substr[:i])) and substr[:i][0] != '0':
                backtrack(substr[i:], current + [substr[:i]])

    backtrack(string, [])
    return len(output) % 10000000007


if __name__ == '__main__':
    string = "30373"
    primeStrings(string)