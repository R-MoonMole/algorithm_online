import sys
sys.stdin = open('11899.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 모든 원소에 대해 make-set 초기화
    p = [i for i in range(N+1)]

    def union_set(x,y):
        a, b = find_set(x), find_set(y)
        if a == b:
            return
        p[a] = b

    def find_set(x):

        # # 기본형
        # if x == p[x]:
        #     return x
        # else:
        #     return find_set(p[x])

        # 경로 압축형
        if x != p[x]:
            p[x] = find_set(p[x])

        return p[x]     # if 걸리면 걸리는대로 p[x]로 되고 안걸리면 그래도 x가 되므로 이렇게 줄여쓴다

    for i in range(0, M*2, 2):
        u, v = arr[i], arr[i + 1]
        # 같은 집합인지 확인
        union_set(u, v)

    # 루트개수 체크
    ans = 0
    for i in range(1, N+1):
        if i == p[i]:
            ans += 1
    print(ans)