# 선형 큐
# 저장소가 있어야 함

Qsize = 4

Q = [0] * Qsize

front = rear = -1

def enqueue(item):
    global rear

    # full-check
    if rear == Qsize -1:
        print('full...')
        return

    rear += 1
    Q[rear] = item

def dequeue():
    global front
    # empty-check -> if front == rear:
    front +=1
    return Q[front]


def is_empty():
    return front == rear


for i in range(5):
    enqueue(i)
print(Q, front, rear)

while front != rear: # empty queue인지 확인
    print(dequeue())