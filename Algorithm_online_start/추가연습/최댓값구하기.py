T = int(input())
max_number = 0

for case_number in range(1, T+1):

    arr = list(map(int, input().split()))
    max_number = 0

    for i in range(10):
        if arr[i] > max_number:
            max_number = arr[i]

    print(f'#{case_number} {max_number}')
