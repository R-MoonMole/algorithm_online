T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    front = rear = 0
    Q = [0] * (N + 1)

    def enqueue(x):
        global rear
        rear = (rear + 1) % (N + 1)
        Q[rear] = x

    def dequeue():
        global front
        front = (front + 1) % (N + 1)
        return Q[front]

    for x in range(1, N+1):
        enqueue(x)

    while front != (rear - 1) % (N + 1):
        dequeue()
        enqueue(dequeue())

    print(f'#{tc} {Q[front]}')
