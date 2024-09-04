# 야구게임

n = int(input()) #도전횟수

def strike_ball(num:str, hint:list):    #hint: [123, 1, 1]
    strike = 0
    ball = 0
    for i in range(3):
        if num[i] in str(hint[0]): 
            # 위치가 일치
            if num[i] == str(hint[0])[i]:
                strike+=1
            # 위치가 불일치
            else:
                ball +=1
        
    return strike, ball

# 민혁의 추측
hint = [list(map(int, input().split())) for _ in range(n)]

#영수의 수 찾기
#모든 경우를 확인해 힌트와 맞는 숫자 찾기
ans = 0
for i in range(1, 10):  #100자리
    for j in range(1, 10):  #10자리
        for k in range(1, 10):  #1자리
            if i==j or i==k or j==k:
                continue
            
            num = str(i)+str(j)+str(k)
            
            # 검증
            cnt = 0
            for c in range(n):  #n번 검증
                strike, ball = strike_ball(num, hint[c])  
                if strike== hint[c][1] and ball == hint[c][2]:
                    # print(c+1, "조건에 일치하는 수:", num)
                    cnt +=1
                else:   # 조건에 맞지 않는 수
                    break
            
            # 검증완료
            if cnt ==n:
                ans +=1
print(ans)