import sys
sys.stdin = open('14696.txt', 'r')

N = int(input())
for _ in range(N):
    a_number = [0, 0, 0, 0]
    b_number = [0, 0, 0, 0]
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    for i in range(1, len(a_arr)):
        a_number[a_arr[i]-1] += 1
    for j in range(1, len(b_arr)):
        b_number[b_arr[j]-1] += 1

    for k in range(3, -1, -1):
        if a_number[k] > b_number[k]:
            print('A')
            break
        elif a_number[k] < b_number[k]:
            print('B')
            break
    else:
        print("D")