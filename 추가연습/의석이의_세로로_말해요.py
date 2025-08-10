T = int(input())

for count_case in range(1, 1+T):
    arr = [str(input()) for _ in range(5)]
    print(arr)

    max_length = 0
    for i in arr:
        if len(i) > max_length:
            max_length = len(i)

    for j in range(1, max_length):
        for k in range(5):
            if j > len(arr[k]):
                arr[k][j]