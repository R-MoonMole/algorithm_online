# BOJ_1713 : 후보 추천하기
# https://www.acmicpc.net/problem/1713


# N = int(input())
# rec = int(input())
# rec_list = list(map(int, input().split()))
# frames = {}
# recommend = 0

N = int(input().strip())
_ = int(input().strip())
votes = list(map(int, input().split()))

frames = {}  # {학생: [추천수, 올린시각]}
time = 0

for s in votes:
    time += 1
    if s in frames:
        frames[s][0] += 1
        continue
    if len(frames) < N:
        frames[s] = [1, time]
    else:
        # 추천수↑, 시각↑ 순으로 최소를 뽑아 제거
        remove = min(frames.items(), key=lambda kv: (kv[1][0], kv[1][1]))[0]
        del frames[remove]
        frames[s] = [1, time]

print(*sorted(frames.keys()))






# for i in rec_list:
#     recommend += 1
#     if i in frames:
#         frames[i][0] += 1
#         continue
#
#     if len(frames) < N:
#         frames[i] = [1, recommend]
#     else:
#         remove = min(frames.items(), key=lambda j: (j[1][0], j[1][1]))[0]
#         del frames[remove]
#         frames[i] = [1, recommend]
#
# ans = sorted(frames.keys())
# print(*ans)



