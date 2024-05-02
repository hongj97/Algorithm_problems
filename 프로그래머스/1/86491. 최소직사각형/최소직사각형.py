def solution(sizes):
    answer = 0
    #초기값
    sizes[0].sort()
    width = sizes[0][0]
    height = sizes[0][1]
    for i in range(len(sizes)):
        sizes[i].sort()
        if sizes[i][0] > width:
            width = sizes[i][0]
        if sizes[i][1] > height:
            height = sizes[i][1]
    # print(width, height)
    answer = width * height
    return answer