def solution(food):
    left = ''
    left_list = [left+str(i)*(food[i]//2) for i in range(1, len(food))]
    left = ''.join(left_list)
    answer = left + '0' + left[::-1]
    return answer