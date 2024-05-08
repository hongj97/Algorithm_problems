x, y, w, h = list(map(int, input().split()))

distance_list = []

#직선거리가 최소
distance_list.append(x-0)
distance_list.append(w-x)
distance_list.append(y-0)
distance_list.append(h-y)

print(min(distance_list))