N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []

def backtracking(x,s):
    if x == M:
        print(*result)
        return
    used = set()
    for i in range(s, N):
        if arr[i] in used:
            continue
        used.add(arr[i])
        result.append(arr[i])
        backtracking(x+1, i)
        result.pop()

backtracking(0,0)