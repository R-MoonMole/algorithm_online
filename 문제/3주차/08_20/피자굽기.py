'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

'''


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    front = rear = 0
    Q = [(-1, -1)] * (N+1)
    next_pizza = N

    def enqueue(x):
        global rear
        rear = (rear + 1) % (N + 1)
        Q[rear] = x

    def dequeue():
        global front
        front = (front + 1) % (N + 1)
        return Q[front]

    for i in range(N):
        enqueue((i + 1, arr[i]))

    while front != (rear - 1) % (N + 1):
        num, cheese = dequeue()
        cheese //= 2

        if cheese == 0:
            if next_pizza < M:
                enqueue((next_pizza + 1, arr[next_pizza]))
                next_pizza += 1
        else:
            enqueue((num, cheese))

    print(f'#{tc} {Q[(front + 1) % (N + 1)][0]}')