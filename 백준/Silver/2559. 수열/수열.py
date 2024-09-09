n, k = map(int, input().split())    #전체날짜수, 연속적인 날짜의 수

temp = list(map(int, input().split()))  #매일 측정한 온도

pref = [0]   #누적합
num = 0
for i in range(len(temp)):
    num += temp[i]
    pref.append(num)

find_max = [pref[j+k]-pref[j] for j in range(0, len(pref)-k)]

print(max(find_max))