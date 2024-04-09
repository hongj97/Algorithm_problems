def solution(arr1, arr2):
    # 초기화
    row = len(arr1)
    col = len(arr1[0])
    answer = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    # print(answer)
    return answer