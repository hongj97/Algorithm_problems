import math

def factors_num(num):
    end_num = int(math.sqrt(num))
    facts=[]
    for i in range(1, end_num+1):
        if num % i == 0: 
            facts.append(i)
            facts.append(num//i)
    return len(set(facts))

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if factors_num(i) % 2== 0: #약수의 개수가 짝수
            answer += i
        else:
            answer -= i #약수의 개수가 홀수
    
    return answer