n = int(input())

ans = []
for _ in range(n):
    num  = int(input())
    if num == 0:
        ans.pop()
    else:
        ans.append(num)
        
#print(ans/
print(sum(ans))