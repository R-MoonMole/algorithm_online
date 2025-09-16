import sys
sys.stdin = open('11902.txt', 'r')

# ==================================

# BFS로 푼 것

# T = int(input())
#
# for tc in range(1, 1+T):
#     N, E = map(int, input().split())
#     graph = [[] for _ in range(N + 1)]
#
#     for _ in range(E):
#         u, v, weight = map(int, input().split())
#         # 유향 그래프
#         graph[u].append((v, weight))
#
#     Q = [0]
#     D = [21e9] * (N + 1)    # 초기화 중요
#     D[0] = 0    # D[출발점] 0으로 초기화
#
#     while Q:
#         u = Q.pop(0)
#         for v, weight in graph[u]:
#             # u --> v 로 가는 경로 체크
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 Q.append(v)
#
#     print(f'#{tc} {D[N]}')

# ==================================

# 다익스트라로 푼것

from heapq import heappush, heappop

T = int(input())

for tc in range(1, 1+T):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        u, v, weight = map(int, input().split())
        # 유향 그래프
        graph[u].append((v, weight))

    Q = []
    D = [21e9] * (N + 1)    # 초기화 중요
    D[0] = 0    # D[출발점] 0으로 초기화
    heappush(Q, (0, 0))     # (거리, 시작정점)

    while Q:
        dist, u = heappop(Q)
        if dist > D[u]:
            continue

        for v, weight in graph[u]:
            # u --> v 로 가는 경로 체크
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                heappush(Q, (D[v], v))

    print(f'#{tc} {D[N]}')
