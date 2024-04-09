def fib(n):
    f_list = [0, 1] #초기값
    if n < 2:
        return f_list[n]
    else:
        for i in range(2, n+1):
            f_list.append(f_list[i-1]+f_list[i-2])
        return f_list[-1]
def solution(n):
    sum = fib(n)
    answer = sum % 1234567
    return answer