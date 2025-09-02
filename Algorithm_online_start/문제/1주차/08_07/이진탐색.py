'''
3
400 300 350
1000 299 578
1000 222 888

'''

T = int(input()) # 테스트 케이스 개수 입력

for count_case_number in range(1, T+1): # 테스트 케이스만큼 반복, 번호 출력에도 사용
    P, Pa, Pb = map(int, input().split()) # 전체 쪽 수 P, A와 B가 찾을 쪽 번호 Pa, Pb 변수에 입력
    left = 1 # 초기 첫 장 변수
    right = P # 초기 마지막장 변수
    A_count = 0 # A가 목표하는 쪽 수를 찾게되는 횟수
    B_count = 0 # B가 목표하는 쪽 수를 찾게되는 횟수
    result = "" # 결과값을 담을 빈 변수

    # A가 원하는 쪽을 찾는 횟수를 구하는 이진 탐색
    while left <= right: # 최소장이 최대장과 같아지거나 넘을때 까지 반복(최악의 수 : 책을 다 이진탐색 하는경우)
        A_count += 1 # 찾는 횟수 누적
        center = (left + right) // 2 # 이진 탐색을 위한 중간페이지 계산 식
        if center == Pa: # 중간페이지가 A가 찾을 쪽 번호일 경우 break
            break
        elif center > Pa: # 중간 페이지가 A가 찾을 쪽 번호보다 큰 경우 right에 center를 넣어 범위를 줄임
            right = center
        else: # 중간 페이지가 A가 찾을 쪽 번호보다 작은경우 left에 center를 넣어 범위를 줄임
            left = center

    left = 1 # A를 찾기위해 사용한 변수 초기화
    right = P

    # B가 원하는 쪽을 찾는 횟수를 구하는 이진 탐색
    while left <= right:
        B_count += 1
        center = (left + right) // 2
        if center == Pb:
            break
        elif center > Pb:
            right = center
        else:
            left = center

    # A_count가 B_count보다 크다는건 A가 더 많은 횟수를 사용하였으므로 B가 이긴것 -> B출력
    if A_count > B_count:
        result = "B"
    # A_count가 B_count보다 작다는건 B가 더 많은 횟수를 사용하였으므로 A가 이긴것 -> A출력
    elif B_count > A_count:
        result = "A"
    # 이외의 경우에는 A_count == B_count 이므로 동점인 경우 -> 0 출력
    else:
        result = "0"

    print(f'#{count_case_number} {result}')