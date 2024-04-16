import math

def solution(n):
    answer = 0
    factors=[]
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            factors.append(i)
            factors.append(int(n/i))
    # print(factors)
    answer = sum(set(factors))
    if n==0:
        answer = 0
    return answer