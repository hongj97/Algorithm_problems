import math
def div_num(n, limit, power): #약수개수 구하는 함수
    div_list = [0]
    for i in range(1, int(math.sqrt(n))+1):
        if n % i ==0:
            div_list.append(i)
            if i != n//i: 
                div_list.append(n//i)
    if len(div_list[1:]) > limit:
        return power
    return len(div_list[1:])
                   
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        num = div_num(i, limit, power)
        answer += num
    # print(answer)
    return answer