def solution(array, commands):
    answer = []
    #sliced array
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        s_array = array[i-1:j]
        # print(s_array)    #잘라온 array
        s_array.sort()
        answer.append(s_array[k-1])
    # print(answer)
    return answer