# BOJ_9086 : 문자열
# https://www.acmicpc.net/problem/9086

T = int(input())
for tc in range(1, 1+T):
    text = input()
    result = ""

    result += text[0]
    result += text[-1]

    print(result)