import sys
sys.stdin = open('24389.txt', 'r')

N = int(input())

Bin = format(N, '032b')
arr = []

for i in Bin:
    if i == '0':
        arr.append('1')
    else:
        arr.append('0')

inv = "".join(arr)

twos = list(inv)
carry = 1






