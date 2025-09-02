for tc in range(1, 11):
    N, arr = map(int, input().split())
    arr = list(map(int,str(arr)))

    new_arr = []
    top = -1

    def my_stack(A):
        global top
        top += 1
        new_arr.append(A)
        if top > 0 and arr[top] == arr[top-1]:
            new_arr.pop()
            new_arr.pop()
            top -= 2

    for i in arr:
        my_stack(i)

    print(new_arr)