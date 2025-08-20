# 백트래킹 -> 모든 후보해(가능한 경우)를 나열하기 위해
# 모든 경우들이 부분집합, 순열, 조합과 관련이 있다.
# 부분 집합의 상태 공간 트리
# 전체 집합의 크기 = N, N번 선택 해야함 -> 트리의 높이가 N
# 매번 선택때 마다 2가지의 선택지가 있음 -> 부분집합에 포함 O or 포함 X

arr = ['A', 'B', 'C']
N = len(arr)
bits = [0] * N

# for i in range(2): # 0 or 1
#     bits[0] = i
#
#     for j in range(2):
#         bits[1] = j
#
#         for k in range(2):
#             bits[2] = k
#
#             print(bits)

def backtrack(k):   # k번 인덱스의 원소에 대한 결정
    if k == N:
        print(bits)
    else:
        # for i in range(2):  # 0 or 1
        #     bits[k] = i
        #     backtrack(k + 1)
        bits[k] = 0
        backtrack(k + 1)

        bits[k] = 1
        backtrack(k + 1)


backtrack(0)

