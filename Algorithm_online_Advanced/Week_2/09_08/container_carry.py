T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())    # N : 컨테이너 수, M : 트럭 수
    W = list(map(int, input().split())) # W : 화물의 무게
    Ti = list(map(int, input().split())) # T : 트럭의 적재 용량
    result = 0

    W.sort(reverse=True)
    Ti.sort(reverse=True)


    for i in range(len(Ti)):
        for j in range(len(W)):
            if Ti[i] >= W[j]:
                result += W[j]
                W.pop(j)
                break
    print(result)

    # def recur(x):
    #     global result
    #
    #     if x == M:
    #         print(f'#{tc} {result}')
    #         return
    #
    #     for i in range(len(Ti)):
    #         for j in range(len(W)):
    #
    #             if W[j] <= Ti[i]:
    #                 result += W[j]
    #                 W.pop(j)
    #                 Ti.pop(i)
    #                 recur(x+1)
    #                 return
    #
    #     print(f'#{tc} {result}')
    # recur(0)