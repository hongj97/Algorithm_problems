def solution(lottos, win_nums):
    same_num = 0    # 일치하는 번호개수
    zeros = 0   # 0인 경우
    for i in lottos:
        if i in win_nums:
            same_num +=1
        if i == 0:
            zeros +=1
    highest = same_num + zeros  # 0이 모두 일치하는 경우
    lowest = same_num   # 0이 모두 일치하지 않는 경우
    if lowest < 2:
        lowest = 1
    if highest == 0:
        highest = 1
    answer = [7-highest, 7-lowest]
    # print(answer)
    return answer

