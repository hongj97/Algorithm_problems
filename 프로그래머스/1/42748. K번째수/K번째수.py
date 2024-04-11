def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        s_array = sorted(array[i-1:j])
        answer.append(s_array[k-1])
    # print(answer)
    return answer