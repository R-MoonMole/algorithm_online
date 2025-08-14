# N = 2
# count = 0
# def make_paper(n, paper): # n: 지금까지 만들어진 종이의 길이, paper: 실제 내용
#     if n > N:
#         return
#     if n == N:
#         global count
#         count += 1
#         print(paper)
#         return
#     else:
#         make_paper(n + 1, paper + 'ㅣ')
#         make_paper(n + 1, paper + 'ㅁ')
#         make_paper(n + 1, paper + '=')
#
# make_paper(0,'')
# print(count)

# n = 1 , 1
# n = 2 , 3
# f(n) = f(n-1) + 2*f(n-2)

def make_paper(n):
    if n == 10:
        return 1
    if n == 20:
        return 3

    return make_paper(n-10) + 2 * make_paper(n-20)

T = int(input())

for count_case in range(1, 1+T):

    N = int(input())
    print(f'#{count_case} {make_paper(N)}')