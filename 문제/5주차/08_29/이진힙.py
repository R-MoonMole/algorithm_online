T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * 10000000
    last = 0
    number = 0

    def enq(n):
        global last
        last += 1
        heap[last] = n

        c = last
        p = c // 2

        while p > 0 and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2

    def P(n):
        global number
        while n > 1:
            n //= 2
            number += heap[n]

    for i in range(N):
        enq(arr[i])

    P(N)
    print(f'#{tc} {number}')