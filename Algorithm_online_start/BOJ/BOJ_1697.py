# BOJ_1697 : 숨바꼭질
# http://acmicpc.net/problem/1697

N, K = map(int, input().split())

def search():

    if N >= K:
        print(N - K)
        return

    MAX = 100000
    dist = [-1] * (MAX + 1)
    q = [N]
    head = 0
    dist[N] = 0

    while head < len(q):
        x = q[head]
        head += 1

        if x == K:
            print(dist[x])
            return

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

search()