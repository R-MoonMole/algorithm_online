T = int(input())

for tc in range(1, 1+T):
    N = float(input())
    result = ""

    while N != 0:
        N *= 2
        X = int(N)
        N -= X
        result += str(X)

        if len(result) > 12:
            result = 'overflow'
            break

    print(f'#{tc} {result}')