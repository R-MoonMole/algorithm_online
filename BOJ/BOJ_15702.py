# BOJ_15702 : 중간고사 채점
# https://www.acmicpc.net/problem/15702

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(N):
    lis = [list(map(int, input().split())) for _ in range(N+1)]
