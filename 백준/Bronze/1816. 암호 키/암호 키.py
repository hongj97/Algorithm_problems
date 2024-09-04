n = int(input()) #입력할 n개의 줄

def chk_num(num:int):   #적절한 암호키인지 판단
    for i in range(2, 1000001):
        if num%i==0: #나누어 떨어지는 경우가 있다면
            return "NO"
        elif i==1000000: #나누어 떨어지는 경우가 없다면
            return "YES"

nums = [int(input()) for _ in range(n)]
for num in nums:
    ans = chk_num(num)
    print(ans)