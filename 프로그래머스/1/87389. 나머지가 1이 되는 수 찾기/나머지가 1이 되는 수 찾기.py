import math
def solution(n):
    answer = 0
    factors =[]
    for i in range(1, int(math.sqrt(n-1))+1):
        if (n-1) % i == 0:
            factors.append(i)
            factors.append((n-1)/i)
    answer = min(factors[1:])
    return answer