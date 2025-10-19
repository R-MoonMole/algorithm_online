while True:
    N = list(map(int, input().strip()))
    if len(N) == 1 and N[0] == 0:
        break
    reverse_N = [0] * len(N)
    for i in range(len(N)):
        reverse_N[i] = N[len(N)-i-1]
    if reverse_N == N:
        print('yes')
    else:
        print('no')

