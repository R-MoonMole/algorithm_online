import sys
sys.stdin = open('14501.txt', 'r')

N = int(input())
time = [0] * (N + 1)
price = [0] * (N + 1)

for i in range(1, 1+N):
    T, P = map(int, input().split())
    time[i] = T
    price[i] = P

dp = [0] * (N + 2)

for i in range(1, 1 + N):
    dp[i + 1] = max(dp[i + 1], dp[i])

    end_day = i + time[i]

    if end_day <= N + 1:
        dp[end_day] = max(dp[end_day], dp[i] + price[i])

print(max(dp))