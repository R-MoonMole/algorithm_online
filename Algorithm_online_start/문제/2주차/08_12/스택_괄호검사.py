T = int(input())

for count_case in range(1, 1+T):
    code = input()
    Parenthesis = []
    Parenthesis_cheak = 1

    for i in code:
        if i == '(' or i == '{' or i == '[':
            Parenthesis.append(i)
        elif i == ')' or i == '}' or i == ']':
            if Parenthesis:
                if i == ')' and Parenthesis[-1] == '(':
                    Parenthesis.pop()
                elif i == '}' and Parenthesis[-1] == '{':
                    Parenthesis.pop()
                elif i == ']' and Parenthesis[-1] == '[':
                    Parenthesis.pop()
                else:
                    Parenthesis_cheak = 0
                    break
            else:
                Parenthesis_cheak = 0
                break
        else:
            continue
    if Parenthesis:
        Parenthesis_cheak = 0

    print(f'#{count_case} {Parenthesis_cheak}')