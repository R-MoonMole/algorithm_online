# # 증가하는 사탕수열
#
# T = int(input())
#
# for tc in range(T + 1):
#     # 3개정도는 따로 받자
#     A, B, C = map(int, input().split())
#
#     #불가능한 케이스를 먼저 지우자
#     if A < 1 or B < 2 or C < 3:
#         print(f'#{tc} {-1}')
#         continue
#
#
#     eat_count = 0
#
#     # B상자 = C상자 - 1
#     if B >= C:
#         eat_count += B - (C - 1)
#         B = C - 1
#
#     # A상자 = B상자 - 1
#     if A >= B:
#         eat_count += A - (B - 1)
#         A = B - 1
#
#     print(f'#{tc} {eat_count}')

# ---------------------------------------------------------------------------

# # 전봇대
#
# T = int(input())
#
# for tc in range(1, 1+T):
#     N = int(input())
#
#     # 1. N 개의 새로운 선이 추가 (기존 선들과 비교)
#     wires = []          # 기존 선들을 저장할 리스트
#     answer_count = 0    # 교차점 수
#
#     for _ in range(N):
#         start, end = map(int, input().split())
#
#         # 기존 선들과 비교 (교차점 비교)
#         for prev_start, prev_end in wires:
#
#         # 1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
#             if start > prev_start and end < prev_end:
#                 answer_count += 1
#
#         # 2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
#             if start < prev_start and end > prev_end:
#                 answer_count += 1
#
#         # 목록에 추가
#         wires.append((start, end))
#     print(f'#{tc} {answer_count}')

# ---------------------------------------------------------------------------

# 탈주범 검거

# 1. BFS로 접근
#   - 이동방향 : 상하좌우
#   - 이동이 불가능한 케이스
#   - [델타 배열 기본] 범위 밖으로 나가면 못감
#   - [방문 기록 기본] 이미 방문한 곳은 못감
#   - 0이면 못감!
#   - [문제 조건]
#       - 현재 내 위치에서 뚫려있는 곳만 이동가능
#       - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
#        -> 이런 케이스들은 델타배열과 동일한 순서 (상하좌우)
#               이동 가능 여부를 기록해두면 좋다.
#
# 2. 방문 기록을 해야한다 (visited)

# 델타배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들 종류에 따라, 이동 가능 여부를 기록
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}
def bfs(R, C):
    q =[(R, C)] # 후보군
    visited[R][C] = 1   # 출발점 초기화

    while q:    # 후보군이 없을 때 까지(더 이상 방문할 수 있는 곳이 없으면 종료)
        now_y, now_x = q.pop(0)
        dirs = types[graph[now_y][now_x]]

        for dir in range(4):
            # 출구가 없으면 다음 방향 확인(continue)
            if dirs[dir] == 0:
                continue

            # 다음 좌표
            new_y = now_y + dy[dir]
            new_x = now_x + dx[dir]

            # 범위 밖이면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 못가는 곳(0)이면 pass
            if graph[new_y][new_x] == 0:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]

            # 현재 상좌 -> next_dirs의 하우가 안뚫렸으면 못간다
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue

            # 현재 하우 -> next_dirs의 상좌가 안뚫렸으면 못간다
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            # L시간 이후는 볼 필요 없다
            if visited[now_y][now_x] + 1 > L:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))



T = int(input())

for tc in range(1, 1+T):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇시간이 걸렸는지를 방문기록에 기록
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')


# from collections import deque
# q = deque([(R,C)])로 바꾸고
# q.pop(0)을 q.popleft()로 바꾸면 덱으로 바뀜



# --------------------------------------------------------------------------

# # 벽돌깨기
#
# # 1. 최소 벽돌
# #  - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다 -> 현재 벽돌 수를 관리
#
# # 2. N번의 구슬을 굴려야 한다
# # - 모든 케이스를 보아야 한다. (12 ^ 4, 약 25 만 번)
# #  - 백트래킹
#     # - 한 번 쏘았을 때 벽돌들이 연쇄로 깨진다.
#     #  - 현재 기준으로 퍼져나가면서 탐색 (BFS)
#     #  - 빈칸 메우기
#
# from collections import deque
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def shoot(cnt, remains, now_arr):
#     global min_blocks
#
#     # 종료 조건: N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
#     if cnt == N or remains == 0:
#         min_blocks = min(min_blocks, remains)
#         return
#
#     # 모든 열에 한 줄 씩 떨구자
#     for col in range(W):
#         # 방법1. 원본을 복사해두고, 다시 되돌리는 방법
#         # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복자 주의)
#         # 2. 원본 리스트의 col 위치에 떨구고
#         # 3. cnt + 1 번 재귀 상태로 이동
#         # 4. 떨구기 전 상태로 복구
#
#         # 방법2. 복구 시간이 없는 방식
#         # 1. col 위치에 떨구기 전 상태를 복사
#         # 2. 복사한 리스트의 col 위치에 떨군다.
#         # 3. cnt + 1 번 상태로 이동할 때, copy_arr 을 함께 전달
#         copy_arr = [row[:] for row in now_arr]
#
#         row = -1
#         # 가장 위 벽돌을 검색
#         for r in range(H):
#             if copy_arr[r][col]:  # 벽돌이 있으면
#                 row = r
#                 break
#
#         if row == -1:  # 벽돌이 없는 열은 pass
#             continue
#
#         # 해당 row, col 의 숫자부터 시작해서 BFS
#         # 행, 열, 숫자를 모두 담아야 한다.
#         q = deque([(row, col, copy_arr[row][col])])
#         now_remains = remains - 1
#         copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 자리
#
#         # 주변 벽돌들을 순차적으로 파괴
#         while q:
#             r, c, p = q.popleft()
#             # 상하좌우의 p 칸을 모두 제거
#             for k in range(1, p):
#                 for i in range(4):
#                     nr = r + (dy[i] * k)
#                     nc = c + (dx[i] * k)
#
#                     # 범위 밖이면 pass
#                     if nr < 0 or nr >= H or nc < 0 or nc >= W:
#                         continue
#
#                     # 벽돌이 없으면 pass
#                     if copy_arr[nr][nc] == 0:
#                         continue
#
#                     q.append((nr, nc, copy_arr[nr][nc]))  # 다음 벽돌 추가
#                     copy_arr[nr][nc] = 0                  # 벽돌 깨짐
#                     now_remains -= 1                      # 숫자 감소
#
#         # 빈칸 메우기
#         for c in range(W):
#             idx = H - 1  # 벽돌이 위치할 index
#             for r in range(H - 1, -1, -1):
#                 if copy_arr[r][c]:
#                     copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
#                     idx -= 1
#
#         shoot(cnt + 1, now_remains, copy_arr)
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     min_blocks = 1e9  # 최소 벽돌 수
#     blocks = 0
#     # 남은 벽돌 수
#     for i in range(H):
#         for j in range(W):
#             if arr[i][j]:
#                 blocks += 1
#
#     shoot(0, blocks, arr)
#     print(f'#{tc} {min_blocks}')