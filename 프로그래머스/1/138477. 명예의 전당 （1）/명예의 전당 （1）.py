def solution(k, score):
    answer = []
    score_list= []
    for i in range(len(score)):
        if i<k: #k일까지 점수는 모두 추가
            score_list.append(score[i])
        else:
            if min(score_list) < score[i]: # 새로운 점수가 크다면 
                #가장 작은 수 제거 후 새로운 점수 추가
                score_list.remove(min(score_list))
                score_list.append(score[i])
        #최하위 점수 추가
        answer.append(min(score_list))        
    # print(answer)
    return answer