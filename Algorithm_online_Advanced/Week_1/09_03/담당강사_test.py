# N = 5
# arr = [i for i in range(N)]

# 모든 분할 위치
# for i in range(1,N-1):
#     for j in range(i+1, N):
#         print(arr[:i], arr[i:j], arr[j:])


arr= ['A', 'B', 'C', 'D']
N = len(arr)
R = 3
pick = [0] * R

def backtrack(k, start):
    if k == R:
        print(pick)

    else:
        for i in range(start, N):
            # k 번째 원소로 i를 선택
            pick[k] = arr[i]
            backtrack(k + 1, i + 1)

backtrack(0, 0)


# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             print(arr[i], arr[j], arr[k])

