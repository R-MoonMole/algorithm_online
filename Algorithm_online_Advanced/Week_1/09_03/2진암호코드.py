import sys
sys.stdin = open("input.txt", "r")

def decoding(S):
    global result

    dict = {
        0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011',
        5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'
    }

    for k, v in dict.items():
        if v == S:
            result += str(k)

    return result

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    x, y = 0, 0
    check = False
    word = ""
    result = ""
    X = ""
    odd, even = 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                x, y = i, j
                check = True
        if check == True:
            break

    for k in range(56):
        word += str(arr[x][y-k])

    word = word[::-1]

    for l in word:
        X += str(l)
        if len(X) == 7:
            decoding(X)
            X = ""

    for a in result[::2]:
        odd += int(a)

    for b in result[1::2]:
        even += int(b)

    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {odd + even}')
    else:
        print(f'#{tc} 0')