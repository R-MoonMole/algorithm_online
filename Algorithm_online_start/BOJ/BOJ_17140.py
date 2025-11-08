def operate(rows):
    new_rows = []
    max_len = 0
    for row in rows:
        count_dict = {}
        for num in row:
            if num == 0:
                continue
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        pairs = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))

        flat = []
        for num, cnt in pairs:
            flat.append(num)
            flat.append(cnt)

        if len(flat) > 100:
            flat = flat[:100]
        new_rows.append(flat)
        max_len = max(max_len, len(flat))

    for i in range(len(new_rows)):

        if len(new_rows[i]) < max_len:
            new_rows[i] += [0] * (max_len - len(new_rows[i]))

    return new_rows

def transpose(arr_A):
    if not arr_A:
        return arr_A
    R, C = len(arr_A), len(arr_A[0])
    return [[arr_A[r][c] for r in range(R)] for c in range(C)]

r, c, k = map(int, input().split())
arr_A = [list(map(int, input().split())) for _ in range(3)]
t = 0
while t <= 100:
    if 0 <= r - 1 < len(arr_A) and 0 <= c - 1 < len(arr_A[0]) and arr_A[r-1][c-1] == k:
        print(t)
        break

    R, C = len(arr_A), len(arr_A[0])
    if R >= C:
        arr_A = operate(arr_A)
    else:
        arr_A_trans = transpose(arr_A)
        arr_A_trans = operate(arr_A_trans)
        arr_A = transpose(arr_A_trans)

    if len(arr_A) > 100:
        arr_A = arr_A[:100]
    if len(arr_A[0]) > 100:
        arr_A = [row[:100] for row in arr_A]

    t += 1

else:
    print(-1)