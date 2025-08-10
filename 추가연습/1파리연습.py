N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0

for i in range(N-M+1):
    for j in range(N-M+1):
        temp_sum = 0
        for x in range(M):
            for y in range(M):
                temp_sum += arr[i+x][j+y]

        if temp_sum > max_sum:
            max_sum = temp_sum

print(max_sum)






