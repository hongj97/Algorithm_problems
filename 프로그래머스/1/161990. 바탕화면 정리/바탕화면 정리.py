def solution(wallpaper):
    answer = []
    
    x = []
    y = []
    for p in range(0, len(wallpaper)):
        if "#" not in wallpaper[p]:
            continue
        loc = wallpaper[p].find('#')    #왼쪽에서 찾기
        last_loc = wallpaper[p].rfind("#")  #오른쪽에서 찾기
        # print(p, loc, p+1, last_loc+1)
        x.append(p)
        y.append(loc)
        x.append(p+1)
        y.append(last_loc+1)
    
    x.sort()
    y.sort()
    answer = [min(x), min(y), max(x), max(y)]
    return answer