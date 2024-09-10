def recur(idx, sour, bitter, use):
    global answer
    if idx==n:
        if use == 0:    #재료를 사용하지 않는 경우
            return
        answer = min(answer, abs(sour-bitter))
        return
    # 재료를 사용할 경우
    recur(idx+1, sour*taste[idx][0], bitter+taste[idx][1], use+1)

    # 재료를 사용하지 않을 경우
    recur(idx+1, sour, bitter, use)

n = int(input()) #재료개수

taste = [list(map(int, input().split())) for _ in range(n)]
answer = 999999999
recur(0, 1, 0, 0)

print(answer)