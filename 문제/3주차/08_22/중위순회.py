import sys; sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = [0] * (N + 1)
    number = 1
    word = []
    result = [] * N
    answer = ""

    for i in range(N):
        for j in range(1,2):
            word.append(arr[i][j])

    def inorder(v):
        global number
        if v > N:
            return
        inorder(v * 2)
        tree[v] = number
        number += 1
        inorder(v * 2 + 1)

    inorder(1)

    for k in range(1, N+1):
        for l in range(N+1):
            if k == tree[l]:
                result.append(word[l-1])
    for n in result:
        answer += n
    print(f'#{tc} {answer}')