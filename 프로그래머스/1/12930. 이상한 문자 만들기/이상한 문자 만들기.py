def solution(s):
    words = list(s)
    chk_even = 0    # 짝수여부 확인
    for i in range(len(words)):
        if words[i] == ' ': #공백이라면
            chk_even = 0 #초기화
            continue
        
        if chk_even %2 ==0:
            words[i] = words[i].upper()     # 짝수
        else:
            words[i] = words[i].lower()     # 홀수
            
        chk_even += 1   
    # print(words)
    answer = ''.join(words)
    return answer