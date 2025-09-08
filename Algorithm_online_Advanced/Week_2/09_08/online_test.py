# # 3명의 친구 부분집합 찾기
# arr = ['O', 'X']
# name = ['MIN', 'CO', 'TIM']
# path = []
#
# def recur(cnt):
#     # 종료 조건 -> 3명을 모두 고려
#     if cnt == 3:
#         print(*path)
#         return
#
#     ## 반복문을 사용하는 방법
#     # for i in range(2):
#     #     path.append(arr[i])
#     #     recur(cnt + 1)
#     #     path.pop()
#
#     # 가지 수(재귀호출 파트)
#     # 1. 부분 집합에 포함되는 경우(O를 추가)
#     path.append(arr[0])
#     recur(cnt + 1)
#     path.pop()
#
#     # 2. 부분 집합에 포함되지 않는 경우(X를 추가)
#     path.append(arr[1])
#     recur(cnt + 1)
#     path.pop()
#
# recur(0) # 0명을 고려한 상태로 시작

# ---------------------------------------------------------------------------

# name = ['MIN', 'CO', 'TIM']
#
# # 두 번째 선택에서는
# # 'MIN' 이라는 친구가 포함된 상태를 저장하면서 진행할 순 엄스까?
# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return
#
#     # 부분 집합에 포함시키는 경우
#     recur(cnt + 1, subset + [name[cnt]])
#     # 부분 집합에 포함시키지 않는 경우
#     recur(cnt + 1, subset)
#
# recur(0, [])

# ---------------------------------------------------------------------------

# arr = [1, 2, 3, 4] # 16개
# print(f'부분 집합의 수 : {1 << len(arr)}')
#
# # i가 의미하는것 : 0~2^n == i번째 부분 집합
# for i in range(1 << len(arr)):  # 부분집합 번호 반복
#     for idx in range(len(arr)): # 각 원소들을 모두 확인
#         if i & (1 << idx):
#             print(arr[idx], end=" ")
#     print()

# ---------------------------------------------------------------------------

# arr = ['A', 'B', 'C']
#
# def get_sub(tar):
#     print(f'target = {tar}', end=' / ')
#     for i in range(len(arr)):
#         # 굳이 16진수를 사용한 이유(사실 1, 0b1, 0b0001 다 된다) -> 비트 연산임을 명시하는 권장 방법
#         if tar & 0x1:
#             print(arr[i], end=' ')
#         tar >>= 1
#
# for target in range(1 << len(arr)):
#     get_sub(target)
#     print()

# ---------------------------------------------------------------------------

# arr = ['A', 'B', 'C', 'D', 'E']
# N = 3
# path = []
#
# def recur(cnt, s):
#     if cnt == N:
#         print(*path)
#         return
#
#     for i in range(s, len(arr)):
#         path.append(arr[i])
#         recur(cnt + 1, i + 1)   # i 번째를 골랐으니 다음 선택은 i+1 부터 고려 (중복을 허용하지 않는 조합)
#         recur(cnt + 1, i)       # i 번째를 골랐으니 다음 선택은 i 부터 고려 (중복을 허용하는 조합)
#         path.pop()
#
# recur(0,0)

# ---------------------------------------------------------------------------

# [문제] 동전의 최소 개수
# 규칙 : 큰 동전부터 나누자
coin_list = [100, 50, 500, 10]
target = 1730
result = 0

# 정렬 연습 : 튜플이라면? 인스턴스 리스트라면? 역순이라면?
#           예) 길이가 우선 정렬, 같은 기리를 사전 순으로 정렬 등..
# list.sort() vs sorted()
coin_list.sort(reverse=True) # 큰 동전부터 사용

for coin in coin_list:
    possible_cnt = target // coin   # 현재 동전으로 가능한 최대 수
    result += possible_cnt          # cnt를 해주고 정답에 더해준다.
    target -= coin * possible_cnt   # 금액을 빼준다.

print(result)

