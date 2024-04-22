def solution(X, Y):
    x = list(X)
    y = list(Y)
    
    answer = ''
    
    num_x = {str(n):0 for n in range(10)}
    num_y = {str(n):0 for n in range(10)}
    
    for i in x:
        num_x[i] +=1
    for j in y:
        num_y[j] +=1
    # print(num_x)
    # print(num_y)
    
    # 더 작은 값이 answer
    for k in range(9, -1, -1):
        num = min(num_x[str(k)], num_y[str(k)])
        # print(f"{k}: {num}")  # 숫자, 개수
        answer += str(k)*num
    
    if answer == '':
        return "-1"
    else:
        if answer[0]=='0':
            answer = '0'
        # print("정답: ", answer)
    return answer