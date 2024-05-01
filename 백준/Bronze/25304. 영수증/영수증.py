x = int(input()) #총금액
n = int(input()) # 물건 종류 수

total_cost = 0

for _ in range(n):
    prod, num = map(int, input().split())
    total_cost = total_cost + prod*num
    
#print(total_cost)
if total_cost == x:
    print("Yes")
else:
    print("No")