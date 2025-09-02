import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    number = list(map(int, input().split()))
    operator = []
    symbols = ['+', '-', '*', '/']
    res = 0
    max_number = 0

    for i in range(4):
        for _ in range(arr[i]):
            operator.append(symbols[i])


    while len(number) >= 2:

        a = number.pop(0)
        op = operator.pop(0)
        b = number.pop(0)

        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = (a / b)

        number.insert(0, res)

    if number[0] > max_number:
        max_number = number[0]

    print(number)








