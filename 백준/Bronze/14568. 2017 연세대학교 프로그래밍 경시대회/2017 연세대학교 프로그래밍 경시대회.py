# 사탕 N개, 사람: 택희(A), 영훈(B), 남규(C)
# 남규 = 영훈 + 2이상
# 사탕을 0개 받는 사람은 없게
# 택희가 받는 사탕의 수는 짝수개

n = int(input())

cnt = 0
for A in range(1, n+1):
    for B in range(1, n+1):
        for C in range(1, n+1):
            if A+B+C==n:    #한명도 빠짐없이 나눠가진 경우
                if C - B >=2 and A%2==0: #남규가 영훈보다 2개 이상 + 택희는 짝수개
                    # print(A, B, C)
                    cnt +=1
# 경우의 수
print(cnt)
