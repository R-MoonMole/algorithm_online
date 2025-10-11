import sys
sys.stdin = open('2527.txt', 'r')

for _ in range(4):
    x1, y1, a1, b1, x2, y2, a2, b2 = map(int, input().split())

    wx = min(a1, a2) - max(x1, x2)
    hy = min(b1, b2) - max(y1, y2)

    if wx > 0 and hy > 0:
        print('a')
    elif wx == 0 and hy == 0:
        print('c')
    elif (wx == 0 and hy > 0) or (wx > 0 and hy == 0):
        print('b')
    else:
        print('d')