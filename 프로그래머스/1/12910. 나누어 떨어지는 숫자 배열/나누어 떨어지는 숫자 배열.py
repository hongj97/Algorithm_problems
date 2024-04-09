def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    answer.sort()   # 오름차순 정렬
    # print(answer)
    
    if len(answer) ==0 :
        answer = [-1]
    return answer