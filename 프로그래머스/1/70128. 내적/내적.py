def solution(a, b):
    answer = 1234567890
    result = [a[i]*b[i] for i in range(len(a))]
    # print(result)
    answer = sum(result)
    return answer