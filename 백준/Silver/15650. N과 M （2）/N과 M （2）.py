def recur(num):
    if num==m+1:
        print(*arr)
        return

    for i in range(num, n+1):
        # 오름차순 수열
        if len(arr) >0 and i <= arr[-1]:
            continue 

        arr.append(i)
        recur(num+1)
        arr.pop()

n, m = map(int, input().split())
arr = []
recur(1)