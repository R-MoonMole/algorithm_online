T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    X = 0
    result = ""

    while N != 0:
        N *= 2
        X = int(N)
        result += str(X)
        N -= X

        if len(result) == 13:
            result = 'overflow'
            break

    print(f'#{tc} {result}')