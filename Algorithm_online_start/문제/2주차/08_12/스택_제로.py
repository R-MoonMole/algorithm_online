T = int(input())

for count_case in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    result_list = []
    result = 0

    for i in range(N):
        if arr[i] != 0:
            result_list.append(arr[i])
        elif arr[i] == 0:
            result_list.pop()

    for j in result_list:
        result += j

    print(f'#{count_case} {result}')