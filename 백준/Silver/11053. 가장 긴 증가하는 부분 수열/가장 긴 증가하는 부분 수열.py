size_a = int(input())
a_arr = list(map(int, input().split()))

dp = [1 for _ in range(size_a)]
for i in range(size_a):
    for j in range(i):
        if a_arr[i] > a_arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
# print(dp)
print(max(dp))
