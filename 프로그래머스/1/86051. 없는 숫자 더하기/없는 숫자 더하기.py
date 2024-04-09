def solution(numbers):
    result = [i for i in range(10) if i not in numbers]
    # print(result)
    answer = sum(result)
    return answer