T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Q = [0] * (M+1)
    front = rear = -1

    def enqueue():
        global rear

        rear += 1
        Q[rear] = arr[i % N]

    def dequeue():
        global front

        front += 1
        return Q[front]

    for i in range(M+1):
        enqueue()
        dequeue()

    print(f'#{tc} {Q[front]}')