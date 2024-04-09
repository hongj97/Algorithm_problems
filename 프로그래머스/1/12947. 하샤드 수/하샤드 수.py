def solution(x):
    # 자릿수 더하기
    num_str = str(x)
    h_number = 0
    num_int = [int(i) for i in num_str]
    # print(num_int)
    
    h_number = sum(num_int)
    if x % h_number ==0:
        return True
    else:
        return False