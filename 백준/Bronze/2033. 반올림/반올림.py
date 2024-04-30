n = int(input())
ans = 10
while n > ans:
    if n%ans >= ans//2:
        n += ans
    n -= (n%ans)
    ans *= 10
print(n)