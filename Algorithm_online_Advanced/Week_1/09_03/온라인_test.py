# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"
    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_number += str(remain)
        n = n // 2

    return binary_number[::-1]

print(decimal_to_binary(0))

def dicimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    if n == 0:
        return "0"
    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 16
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n = n // 16

    return hexadecimal_number

print(dicimal_to_hexadecimal(51642))

# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number

print(binary_to_decimal('11101'))

# 내장함수도 있음
print(hex(100)) # 16진수
print(bin(100)) # 2진수

print('----------------------')
print(1 << 1, bin(1 << 1))
print(1 << 4, bin(1 << 4))
print(7 >> 1, bin(7 >> 1))

num = 2
for _ in range(5):
    print(num, end=" ")
    num = num << 1
print()

# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [7, 1, 3, 5] # 16개
print(f'부분 집합의 수 : {1 << len(arr)}')

# 2. 전체 부분집합을 구할 수 있다.
for i in range(1 << len(arr)):  # 부분집합 번호 반복
    for idx in range(len(arr)): # 각 원소들을 모두 확인
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()

# 3. 응용, 합이 10인 부분집합만 구해라
arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):  # 부분집합 번호 반복
    subset = []
    total = 0

    for idx in range(len(arr)): # 각 원소들을 모두 확인
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'합이 10인 부분집합 : {subset}')














