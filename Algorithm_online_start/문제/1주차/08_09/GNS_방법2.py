T = int(input())

for _ in range(T):
    case_number, test_length = input().split()
    test_length = int(test_length)
    test_case = input().split()

    number_list = [0,0,0,0,0,0,0,0,0,0]
    number_list2 = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in test_case:
        if i == 'ZRO':
            number_list[0] += 1
        elif i == 'ONE':
            number_list[1] += 1
        elif i == 'TWO':
            number_list[2] += 1
        elif i == 'THR':
            number_list[3] += 1
        elif i == 'FOR':
            number_list[4] += 1
        elif i == 'FIV':
            number_list[5] += 1
        elif i == 'SIX':
            number_list[6] += 1
        elif i == 'SVN':
            number_list[7] += 1
        elif i == 'EGT':
            number_list[8] += 1
        elif i == 'NIN':
            number_list[9] += 1

    print(case_number)
    for j in range(10):
        c = number_list[j]
        while c > 0:
            print(number_list2[j], end=" ")
            c -= 1

    print()