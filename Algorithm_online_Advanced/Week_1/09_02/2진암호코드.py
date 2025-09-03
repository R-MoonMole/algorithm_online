import sys
sys.stdin = open("input2.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    count = -1
    key = ''
    result = ''
    text = ''
    x, y = 0, 0
    odd = 0
    even = 0

    def decoding(X):
        global result
        ratio = ""
        zero_count = 0
        one_count = 0
        dict = {
            '0': '3211', '1': '2221', '2': '2122', '3': '1411',
            '4': '1132', '5': '1231', '6': '1114', '7': '1312',
            '8': '1213', '9': '3112'
        }

        for i in X:

            if i == '0':
                if one_count != 0:
                    ratio += str(one_count)
                    zero_count += 1
                    one_count = 0
                else:
                    zero_count += 1

            elif i == '1':
                if zero_count != 0:
                    ratio += str(zero_count)
                    one_count += 1
                    zero_count = 0
                else:
                    one_count += 1

        if one_count !=0:
            ratio += str(one_count)
        elif zero_count != 0:
            ratio += str(zero_count)

        for k, v in dict.items():
            if v == ratio:
                result += k
        return result

    for i in range(N):
        if count != -1:
            for l in range(56):
                key += arr[x][y - l]
            break

        for j in range(M):
            if arr[i][j] == '1':
                count = 1
                x, y = i, j

    key = key[::-1]

    for l in key:
        text += l
        if len(text) == 7:
            decoding(text)
            text = ''

    for a in result[::2]:
        odd += int(a)
    for b in result[1::2]:
        even += int(b)

    if ((odd*3)+even)%10 != 0:
        print(f'#{tc} 0')
    elif ((odd*3)+even)%10 == 0:
        print(f'#{tc} {odd+even}')