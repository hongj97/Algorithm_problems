def solution(citations):
    answer = 0
    # 논문 n편 중, h번 이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하 인용
    citations.sort() # 정렬
    
    for i in range(len(citations)-1, -1, -1):
        # print(f"{citations[i]}번 인용된 논문 {len(citations)-i}개")
        if citations[i] < len(citations)-i:
            break
        answer = len(citations)-i
    return answer