def solution(s):
    answer = ''
    s=sorted(s, reverse=True)
    # print(s)
    answer = ''.join(s)
    return answer