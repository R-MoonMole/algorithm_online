# 원형 큐
Qsize = 4       # 선형은 front가 가리키는 곳이 -1이기때문에 Qsize가 4개면 데이터를 4개 넣을 수 있지만
                # 원형은 front가 가리키는 곳이 0이기에 Qsize가 4개면 데이터를 3개 넣을 수 있다.
Q = [0] * Qsize
front = rear = 0

def enqueue(item):
    global rear
    # full-check
    if (rear + 1) % Qsize == front:
        print('full...')
        return

    rear = (rear + 1) % Qsize
    Q[rear] = item

def dequeue():
    global front
    # empty-check -> if front == rear:
    front = (front + 1) % Qsize
    return Q[front]


def is_empty():
    return front == rear


def print_queue():
    f, r = front, rear
    print('[', end=' ')
    while f != r:
        f = (f + 1) % Qsize
        print(Q[f], end=' ')
    print(']')

enqueue(1); print_queue()
enqueue(2); print_queue()
enqueue(3); print_queue()
enqueue(4); print_queue()

print(dequeue()); print_queue()
print(dequeue()); print_queue()

enqueue(5); print_queue()