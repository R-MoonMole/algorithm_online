T = int(input())

for count_case in range(1, 1+T):
    A, B = input().split()
    len_A = 0 # len(text)
    len_B = 0 # len(pattern)

    for _ in A: # len(text)을 구하기 위한 반복문
        len_A += 1

    for _ in B: # len(pattern)을 구하기 위한 반복문
        len_B += 1

    total_len = len_A # 초기 전체 문자열의 길이(타이핑 해야하는 길이)
    for i in range(0, len_A - len_B + 1):
        for j in range(len_B):
            if A[i+j] != B[j]: # index j부터 시작한 pattern 문자가 index i+j부터 시작한 text문자열과 다르면
                break # break

        else: # 같은 경우에는 전체 문자열의 길이에서 len_B를빼고 1을 더함(len_B를 1로 치환한 느낌)
            total_len = total_len - len_B + 1


    print(f'#{count_case} {total_len}')
