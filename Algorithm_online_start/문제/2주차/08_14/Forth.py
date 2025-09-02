T = int(input())

for count_case in range(1, 1+T):
    stack = [0] * 258
    top = -1
    arr = input().split()
    result = ""
    for i in arr:
        if i == '.':
            if top == 0:
                result = stack[0]
            else:
                result = 'error'
            break
        elif i not in '+-*/':
            top += 1
            stack[top] = i
        elif i in '+-*/':
            if top < 1:
                result = 'error'
                break
            x = int(stack[top])
            top -= 1
            y = int(stack[top])
            top -= 1
            if i == '+':
                top += 1
                stack[top] = x + y
            elif i == '-':
                top += 1
                stack[top] = y - x
            elif i == '*':
                top += 1
                stack[top] = x * y
            elif i == '/':
                top += 1
                stack[top] = y // x
        else:
            top += 1
            stack[top] = i

    print(f'#{count_case} {result}')