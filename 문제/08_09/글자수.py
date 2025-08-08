'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

'''
T = int(input()) # 테스트 케이스 입력

for case_number in range(1, 1+T): # 테스트 케이스 숫자만큼 반복
    str1 = list(input()) # str1 입력
    str2 = list(input()) # str2 입력

    count_str1 = 0  # 각 변수 초기값 설정
    count_str2 = 0
    count_result = 0
    result = 0

    # 주어진 str1, str2의 길이를 len 내장함수 없이 구하기
    for i in str1:
        count_str1 += 1
    for j in str2:
        count_str2 += 1

    # str1과 str2의 각각을 비교, result에 몇개가 들어있는지 넣어줌
    for k in range(count_str1):
        for l in range(count_str2):
            if str1[k] == str2[l]:
                count_result += 1

            if result < count_result:
                result = count_result
        count_result = 0 # 한바퀴 돌 때마다 변수 초기화

    print(f'#{case_number} {result}')