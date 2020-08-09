import math

# Whew, problem statement sure made the pattern hard. This is a
# Fibo sequence question.

def maximum_lambs(lambs):
    x = int(math.log(abs(lambs), 2))
    return x
    
def minimum_lambs(lambs):
    return int(math.ceil(math.log((lambs + 1 + 0.5)*math.sqrt(5), (1+math.sqrt(5)) / 2)) - 3)
    
def solution(total_lambs):
    return minimum_lambs(total_lambs) - maximum_lambs(total_lambs)
    # Your code here

if __name__ == "__main__":
    print(solution(143))
    print(solution(10))