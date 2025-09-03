import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N, M = input().split()
    N = int(N)
    real = ""

    result = int(M, 16)

    while result > 0:
        if result % 2 == 1:
            real += '1'
            result //= 2
        else:
            real += '0'
            result //= 2

    if len(real) % 4 != 0:
        real += '0'
    real = real[::-1]
    print(f'#{tc} {real}')


'''
print(bin(int('47FE',16)))
이렇게 하면 0b1000111111111110 이렇게 나옴...

아니면 딕셔너리 사용
hex_dict = {
    '0': '0000', '1':'0001', '2': '0010', '3':'0011',
    '4': '0100', '5':'0101', '6': '0110', '7':'0111', 
    '8': '1000', '9':'1001', 'A': '1010', 'B':'1011', 
    'C': '1100', 'D':'1101', 'E': '1110', 'F':'1111', 
    }
for ch in hex_str:
    bin_str += hex_dict

'''