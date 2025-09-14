# 종료 조건 : N개의 행을 모두 고려하면 종료
# 가지의 수 : N개의 열

def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]:
            return False
    # 2. 좌상단 대각선에 놓은 적이 있는가? ( \ )
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # # 이걸 for문으로 하고싶으면
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? ( / )
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    return True

def recur(row):
    global answer
    if row == N:
        answer += 1
        return

    for col in range(N):
        # 가지치기 : 원래 같은 열을 못 고르도록
        # --> 유망하지 않은 케이스 모두 삭제(세로, 대각선) (가로는 이미 col로 볼 수 있어서 제외)
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        recur(row + 1)
        visited[row][col] = 0

N = 4
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')

N = 8
answer = 0
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')

N = 12
answer = 0
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')

# ==========================================================================

# arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
#
# # 그래프 처럼 저장하는 방식
# nodes = [[] for _ in range(14)]
#
# for i in range(0, len(arr), 2):
#     parent_node = arr[i]
#     child_node = arr[i+1]
#     nodes[parent_node].append(child_node)
#
# # 자식이 없는 걸 표현하기 위해 None을 삽입
# for li in nodes:
#     for _ in range(len(li), 2):
#         li.append(None)
#
# def order(node):
#     if node == None:
#         return
#
#     # nodes[node] : node에 연결된 번호들 (자식 번호들)
#     # nodes[node][0] : 첫 번째 자식 번호
#     # nodes[node][0] : 두 번째 자식 번호
#
#     print(node, end=" ") # 전위순회
#     order(nodes[node][0])
#     # print(node, end=" ") # 중위순회
#     order(nodes[node][1])
#     # print(node, end=" ") # 후위순회
#
# order(1) # 1번 노드부터 시작

# ==========================================================================












