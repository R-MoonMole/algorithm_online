'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''
T = int(input())
count_case_number = 1

for _ in range(T):

    K, N, M = map(int, input().split())
    M_location = list(map(int, input().split()))
    bus_station = [0] * (N+5)
    charge_count = 0
    btw = K


    for i in range(0, M):
        bus_station[M_location[i]] = 1

    for j in range(0, N+1):
        if btw == 0:
            charge_count = 0
            break

        if bus_station[j] == 0:
            btw -= 1
        elif bus_station[j] == 1:
            btw = K
            charge_count += 1

    print(f'#{count_case_number} {charge_count}')


    # for j in range(0, N+1):
    #     btw = K
    #     if bus_station[j] == 0:
    #         btw -= 1
    #     elif bus_station[j] == 1:
    #         for k in range(1, K+1):
    #             if bus_station[j+k] != 1:
    #                 continue
    #             elif bus_station[j+k] == 1:
    #                 if bus_station[]










    # print(f'#{count_case_number} {result}')
    # count_case_number += 1
