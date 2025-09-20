# BOJ_11729 : 하노이 탑 이동순서
# https://www.acmicpc.net/problem/11729

def hanoi(n, start, end, sub, out):
    if n == 1:
        out.append((start, end))
        return
    hanoi(n-1, start, sub, end, out)
    out.append((start, end))
    hanoi(n-1, sub, end, start, out)

N = int(input())
moves = []
hanoi(N, 1, 3, 2, moves)

print(len(moves))
for a, b in moves:
    print(a, b)
