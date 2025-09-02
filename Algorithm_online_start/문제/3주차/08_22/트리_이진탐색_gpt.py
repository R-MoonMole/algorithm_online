T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [0] * (N+1)
    number = 1

    def inorder(v):
        global number
        if v > N:
            return
        inorder(v * 2)
        arr[v] = number
        number += 1
        inorder(v * 2 + 1)

    inorder(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')