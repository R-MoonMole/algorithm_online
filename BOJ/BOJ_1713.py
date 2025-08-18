# BOJ_1713 : 후보 추천하기
# https://www.acmicpc.net/problem/1713


N = int(input())
rec = int(input())
rec_list = list(map(int, input().split()))
frames = {}
recommend = 0

for i in rec_list:
    recommend += 1
    if i in frames:
        frames[i][0] += 1
        continue

    if len(frames) < N:
        frames[i] = [1, recommend]
    else:
        remove = min(frames.items(), key=lambda j: (j[1][0], j[1][1]))[0]
        del frames[remove]
        frames[i] = [1, recommend]

ans = sorted(frames.keys())
print(*ans)



