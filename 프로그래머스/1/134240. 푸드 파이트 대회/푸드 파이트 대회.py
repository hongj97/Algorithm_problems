def solution(food):
    answer = ''
    f_dict = {i:j for i, j in enumerate(food)}
    left = ''
    for i in range(1, len(food)):
        num = f_dict[i]
        if num % 2 != 0:
            num = num -1 # 개수가 홀수라면 1제외
        left = left + str(i)*(num//2)
    right = left[::-1]
    answer = left + '0' + right
    return answer