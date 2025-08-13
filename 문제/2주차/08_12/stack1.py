for count_case in range(1, 11):

    N, text = input().split()
    N = int(N)
    stack_text = []
    result = ''
    for i in text:
        stack_text.append(i)

    while True:
        check = 0

        for j in range(N - 1):
            if stack_text[j] == stack_text[j+1]:
                stack_text.pop(j)
                stack_text.pop(j)
                N -= 2
                check = 1
                break

        if check == 0:
            break

    for k in stack_text:
        result += k
    print(f'#{count_case} {result}')