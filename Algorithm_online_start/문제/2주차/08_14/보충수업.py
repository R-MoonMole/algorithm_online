# 재귀 호출은 기본적으로 반복이다.
    # 분할 정복 => 이진 탐색
    # DFS
    # 재귀호출(점화식구현) + 메모이제이션
    # 백트레킹

# i = 0
# while i < 3:
#     print('hello!')
#     i += 1


# 재귀호출은 함수 밖의 매개변수를 통해서 판단해야함, 함수 내부에 있는 변수로 범위를 지정하면 안된다.
cnt = 0
def print_hello(i, N):
    if i == N:
        global cnt
        cnt += 1
        return
    else:
        print_hello(i + 1, N)
        print_hello(i + 1, N)

print_hello(0, 4)
print(cnt)