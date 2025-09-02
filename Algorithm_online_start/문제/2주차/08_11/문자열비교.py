T = int(input())

for count_case in range(1, 1+T):
    str1 = input() # pattern
    str2 = input() # text
    str1_count = 0 # len(pattern)
    str2_count = 0 # len(text)
    found = 0 # text안에 pattern이 있는지 출력용 초기값 -> 있으면 1 없으면 0

    # len 함수 안쓰고 str의 길이를 구하기 위한 반복문
    for _ in str1:
        str1_count += 1
    for _ in str2:
        str2_count += 1

    for i in range(0, str2_count - str1_count + 1): # 범위가 0부터 text길이 - pattern길이 + 1
        for j in range(str1_count):
            if str2[i + j] != str1[j]: # str1은 그대로, str2는 위치가 i씩 올라가면서 계속 반복
                break
        else:
            found = 1

    print(f'#{count_case} {found}') # 출력

# def brute_force(p, t):
#     i = 0
#     j = 0
#     M = len(p)
#     N = len(t)
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return 1
#     else:
#         return 0