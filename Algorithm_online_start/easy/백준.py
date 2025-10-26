import sys
sys.stdin = open('asdf.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque()