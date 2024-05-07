def is_prime(a):
    for i in range(2, int(a/2)+1):
        # print(f"현재수: {i}, 나머지: {a%i}")
        if a % i == 0: #나누어떨어지면 소수가 아니다
            return False
    return True

def solution(nums):
    answer = 0
    
    sum = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                # print(f"{sum}은 소수가 {is_prime(sum)}")
                if is_prime(sum):
                    answer +=1
    
    return answer