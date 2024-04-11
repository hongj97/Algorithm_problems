def solution(s, skip, index):
    answer = ''
    skip_list = list(skip)
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip_list] #알파벳 리스트 생성
    # print(alpha)
    
    str1 = list(s)
    moved_alpha = [alpha[(alpha.index(i)+index)%len(alpha)] for i in str1]
    answer = ''.join(moved_alpha)
    return answer