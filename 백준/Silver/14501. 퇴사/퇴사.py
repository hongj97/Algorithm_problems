N = int(input()) #날짜

T = [0]*N
P = [0]*N

#입력배열 완성
for n in range(0, N):
    t, p = map(int, input().split())
    T[n] = t
    P[n] = p

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if (i + T[i]) <= N: #날짜를 안넘을 때
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])