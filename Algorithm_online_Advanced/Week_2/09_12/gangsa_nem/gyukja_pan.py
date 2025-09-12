import sys
sys.stdin = open('2819.txt', 'r')

dy = [-1, 1, 0 ,0]
dx = [0, 0, -1, 1]

# 1. 종료조건 : 숫자 7자리일때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):
    if len(number) == 7:    # 7자리인 경우 종료
        result.add(number)  # set에 추가
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면 다음방향 확인(continue)
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        # 중복 되어도 상관없으니 다음 위치로 이동
        recur(ny, nx, number + matrix[ny][nx])

T = int(input())

for tc in range(1, 1+T):
    matrix = [input().split() for _ in range(4)]
    result = set()

    # 7자리 만드는 코드
    # -> 4 * 4 가 모두 출발점이 될 수 있다
    for start_y in range(4):
        for start_x in range(4):
            recur(start_y, start_x, matrix[start_y][start_x])

    print(f'#{tc} {len(result)}')