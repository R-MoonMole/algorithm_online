T = 10

for count_case in range(1, 1+T):
    N = int(input())
    stack = [0] * N
    arr = input().split('+')
    postfix_notation = ''
    count = 0
    top = -1

    for _ in arr:
        count += 1

    for i in range(count):
        if i == 0:
            postfix_notation += arr[i]
        else:
            postfix_notation += arr[i]
            postfix_notation += "+"

    for j in postfix_notation:
        if j == '+':
            x = stack[top]
            top -= 1
            y = stack[top]
            stack[top] = x + y
        else:
            top += 1
            stack[top] = int(j)

    print(f'#{count_case} {stack[top]}')