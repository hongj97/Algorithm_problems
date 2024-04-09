import math

def count_brown(row, col):
    return row*2 + col*2 + 4

def find_pair(num, brown):
    col = 0   # 가로
    row = 0  # 세로
    for i in range(1, int(math.sqrt(num))+1):
        if num % i ==0:
            col = num // i
            row = i
            if count_brown(row,col) == brown:   # 원하는 쌍을 찾았으면 반복문 탈출
                # print(f"가로: {col}, 세로: {row}, {count_brown(row, col)}")   #중간확인
                break
            
    return row, col

def solution(brown, yellow):
    answer = []
    
    # 곱해서 yellow를 만들 수 있는 두 수 찾기
    row, col = find_pair(yellow, brown) # 가로가 col, 세로가 row
    answer = [col+2, row+2] # yellow 영역의 가로 세로에 2줄씩 추가
    return answer