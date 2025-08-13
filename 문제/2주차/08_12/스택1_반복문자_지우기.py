T = int(input())

for count_case in range(1, 1+T):

    stack_text = []
    text = input()
    result = 0

    for i in text:
        stack_text.append(i)

    while True:
        check = 0
        text_len = 0
        for j in stack_text:
            text_len += 1

        for k in range(text_len-1):

            if stack_text[k] == stack_text[k+1]:
                stack_text.pop(k)
                stack_text.pop(k)
                check = 1
                break

        if check == 0:
            break

    for l in stack_text:
        result += 1

    print(f'#{count_case} {result}')