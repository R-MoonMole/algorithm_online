import sys; sys.stdin = open('input.txt')

for _ in range(1, 11):
    T = int(input())
    arr = list(map(int,input().split()))
    N = 8
    Q = [0] * (N+1)
    front = rear = 0

    def enqueue(x):
        global rear
        rear = (rear + 1) % (N + 1)
        Q[rear] = x

    def dequeue():
        global front
        front = (front + 1) % (N + 1)
        return Q[front]

    for x in arr:
        enqueue(x)

    while True:
        for i in range(1,6):
            x = dequeue()
            x -= i
            if x <= 0:
                enqueue(0)
                break
            enqueue(x)
        else:
            continue
        break
    result = [Q[(front + 1 + i) % (N + 1)] for i in range(N)]
    print(f'#{T}', *result)
