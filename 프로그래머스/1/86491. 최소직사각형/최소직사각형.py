def solution(sizes):
    answer = 0
    
    width_list = [min(sizes[i]) for i in range(len(sizes))]
    height_list = [max(sizes[i]) for i in range(len(sizes))]
    
    width = max(width_list)
    height = max(height_list)

    answer = width*height
    return answer