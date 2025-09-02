'''
10
0 0 254 185 76 227 84 175 0 0
10
0 0 251 199 176 27 184 75 0 0
11
0 0 118 90 243 178 99 100 200 0 0

'''


for test_case_number in range(1, 11):

    result = 0

    N = int(input())
    Height = list(map(int, input().split()))

    for i in range(2, N-2):

        if max(Height[i-2],Height[i-1], Height[i], Height[i+1], Height[i+2]) == Height[i]:

           result += Height[i]-max(Height[i-2], Height[i-1], Height[i+1], Height[i+2])

    print(f'#{test_case_number} {result}')