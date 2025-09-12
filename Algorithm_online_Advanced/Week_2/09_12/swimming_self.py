import sys
sys.stdin = open('1952(2).txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    swim_day, swim_month, swim_3month, swim_year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    min_cost = 10e20

    def swimming(month, cost):
        global min_cost
        if month > 12:
            if min_cost > cost:
                min_cost = cost
            return

        if cost >= min_cost:
            return

        swimming(month + 1, cost + (arr[month] * swim_day))
        swimming(month + 1, cost + swim_month)
        swimming(month + 3, cost + swim_3month)
        swimming(month + 12, cost + swim_year)

    swimming(1, 0)
    print(f'#{tc} {min_cost}')