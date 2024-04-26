def solution(arr):
    arr.remove(min(arr))
    answer = arr
    if len(answer) == 0:
        return [-1]
    return answer