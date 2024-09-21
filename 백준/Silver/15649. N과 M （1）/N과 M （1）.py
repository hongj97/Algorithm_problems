#1부터 n까지 중복 없이 m개 고르기
def recur(number):
    if number==m:
        print(*arr)
        return

    for i in range(1, n+1):
        #중복 없이
        if i in arr:
            continue
        arr.append(i)
        recur(number+1)
        arr.pop()
        
n, m = map(int, input().split())
arr = []

recur(0)