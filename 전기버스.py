'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''

T = int(input()) # 노선수 input
count_case_number = 1 # 테스트 케이스 번호 출력용

for _ in range(T):

    K, N, M = map(int, input().split()) # K = 최대 이동가능 정류장, N = 종점, M = 충전소 수 변수
    M_location = list(map(int, input().split())) # 충전소가 설치 된 정류장 번호 리스트
    bus = 0 # 버스의 현재 위치 파악용 변수
    total_move = bus + K # 버스의 총 이동 가능한 거리 변수
    charge_station = 0 # 충전소 위치 변수
    result = 0 # 결과 변수

    while (total_move < N): # 버스의 총 이동거리가 종점을 지날때까지 반복

        for i in M_location: # 충전소가 설치된 정류장 리스트를 반복문으로 꺼내옴

            if bus < i <= total_move: # 버스의 현재위치와 이동가능한 거리 안에 충전소가 있으면 다음 충전소 위치 변수를 가져옴
                charge_station = i

            elif total_move < i: # 총 이동 가능거리보다 충전소가 멀면 break
                break

        if charge_station == -1: # charge_station이 -1일때(while문 돌때 위에 i가 입력이 안되는 경우(충전소가 먼 경우) break
            result = 0
            break

        # while문 돌 때마다 초기화되는 변수
        bus = charge_station
        total_move = bus + K
        result += 1
        charge_station = -1

    print(f'#{count_case_number} {result}') # 결과 출력
    count_case_number += 1
