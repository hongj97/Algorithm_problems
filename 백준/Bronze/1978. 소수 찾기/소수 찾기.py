# 소수 찾기

n = int(input())
num_list = list(map(int, input().split()))

#소수 확인
cnt = 0
for num in num_list:
    prime_chk = 0
    end_num = int(num**0.5)+1 #num이 홀수
    if int(num**0.5) % 2==0: #num이 짝수
        end_num=int(num**0.5)+1
    if num != 1:
        for i in range(2, end_num):
            if num % i == 0: #소수가 아닌 경우
                break
            else: #소수인 경우
                prime_chk +=1
        if prime_chk == (end_num-2):
            cnt +=1
print(cnt)