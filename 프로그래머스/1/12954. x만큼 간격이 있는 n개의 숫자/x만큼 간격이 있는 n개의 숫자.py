def solution(x, n):
    # x씩 n번 증가
    answer = [x+x*i for i in range(n)]
    return answer