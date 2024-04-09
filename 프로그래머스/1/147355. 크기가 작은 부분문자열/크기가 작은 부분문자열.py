def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        chk_num = t[i:i+len(p)]
        
        if int(chk_num) <= int(p):
            answer +=1
            # print(f"{chk_num}<={p}, {answer}번째")
    
    return answer