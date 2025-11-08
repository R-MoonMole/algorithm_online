import sys
sys.stdin = open('swea_1244.txt', 'r')

def dfs(number, count):
    global result
    if count == K:
        result = max(result, int(''.join(number)))
        return

    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]
            X = ''.join(number)
            if (X, count + 1) not in visited:
                visited.add((X, count + 1))
                dfs(number, count + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, 1+T):
    number, K = input().split()
    K = int(K)
    number = list(number)
    visited = set()
    result = 0
    dfs(number, 0)
    print(f'#{tc} {result}')
