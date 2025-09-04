# path = []
# N = int(input())
#
# def run(lev):
#     if lev == N:
#         print(path)
#         return
#     for i in range(1,4):
#         path.append(i)
#         run(lev + 1)
#         path.pop()
#
# run(0)

# def KFC(x):
#     if x == 6:
#         return
#     print(x, end=' ')
#     KFC(x+1)
#     print(x, end=' ')
#
# KFC(0)
# print('끝')

# ==========================================================================================
# # 중복 순열
# # [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다
#
# path = []   # used, visited... -> 뽑은 카드들을 저장
#
# # 기저조건(종료조건) : 2개의 카드를 모두 뽑았다면 종료
# # - 시작점 : 0개의 카드를 고른 상태부터 시작
# # 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.
#
#
#
# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     # 카드 0, 1, 2 중 하나를 선택
#     for num in range(1,7):
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#
#
#     # path.append(0)
#     # recur(cnt + 1)
#     # path.pop()
#     #
#     # path.append(1)
#     # recur(cnt + 1)
#     # path.pop()
#     #
#     # path.append(2)
#     # recur(cnt + 1)
#     # path.pop()
#
# recur(0)

# ==========================================================================================

# 중복 없는 일반 순열
path = []
# used = [False, False, False, False, False, False] # 고를 수 있는 수 만큼 만들어 준다.
# used = [False] * N    # N개의 카드 종류가 있는 경우
used = [False] * (7)    # 1~6까지의 카드 숫자 사용 여부를 기록 (False 대신 0도 가능, 인덱스 0은 버린다) -> 주로 씀

def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1, 7):
        # in 을 쓰면 리스트 전부를 다 확인

        # if num in path: -> 이미 path에 있는 숫자는 생략
        # continue
        if used[num]:
            continue

        used[num] = 1
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = 0

recur(0)

# ==========================================================================================

# 주사위 3개를 던져서 합이 10 이하인 케이스의 수

# path = []   # 주사위 눈을 저장을 할 필요가 없으니 굳이 저장을 해야할까...? 흠...
# result = 0
#
# def recur(cnt, total):
#     global result
#
#     # 이미 10을 넘은 경우는 더 볼 필요가 없다
#     # 기저 조건에서 많은 경우의 수를 줄일 수 있다
#     if total > 10:
#         return
#
#     if cnt == 3:
#         result += 1
#         return
#
#     for num in range(1, 7):
#         recur(cnt + 1, total + num)
#
# recur(0, 0)
# print(result)

# ==========================================================================================

# # [A, J, Q, K]가 각각 넉넉히 있다
# # 카드 5장을 뽑았을 때, 같은 종류의 카드가 3장 연속으로 나오는 경우의 수
#
# cards = ['A', 'J', 'Q', 'K']
# path = []
# result = 0
#
# # 연속된 3개의 같은 카드가 나오면 return True, 아니면 False
# def count_three():
#     # 3개정도는 하드코딩도 충분히 가능하다 = Simple is best
#     if path[0] == path[1] == path[2]: return True
#     if path[1] == path[2] == path[3]: return True
#     if path[2] == path[3] == path[4]: return True
#     return False
#
# def recur(cnt):
#     global result
#
#     if cnt == 5:
#         # todo : 연속된 3개가 나오면 counting
#         if count_three():
#             result += 1
#             print(*path)
#         return
#
#     # 카드 중 하나를 선택
#     for idx in range(len(cards)):
#         path.append(cards[idx])
#         recur(cnt + 1)
#         path.pop()
#
# recur(0)
# print(result)
#
#












