T = int(input())
ZRO = 0
ONE = 1
TWO = 2
THR = 3
FOR = 4
FIV = 5
SIX = 6
SVN = 7
EGT = 8
NIN = 9

for _ in range(T):
    case_number, test_length = input().split()
    test_length = int(test_length)
    test_case_list = list(input().split())

    for i in range(test_length):
        if test_case_list[i] == 'ZRO':
            test_case_list[i] = 0
        elif test_case_list[i] == 'ONE':
            test_case_list[i] = 1
        elif test_case_list[i] == 'TWO':
            test_case_list[i] = 2
        elif test_case_list[i] == 'THR':
            test_case_list[i] = 3
        elif test_case_list[i] == 'FOR':
            test_case_list[i] = 4
        elif test_case_list[i] == 'FIV':
            test_case_list[i] = 5
        elif test_case_list[i] == 'SIX':
            test_case_list[i] = 6
        elif test_case_list[i] == 'SVN':
            test_case_list[i] = 7
        elif test_case_list[i] == 'EGT':
            test_case_list[i] = 8
        elif test_case_list[i] == 'NIN':
            test_case_list[i] = 9

    for j in range(test_length):
        for k in range(j, test_length):
            min_idx = k
            if test_case_list[min_idx] > test_case_list[j]:
                min_idx = j
            test_case_list[j], test_case_list[min_idx] = test_case_list[min_idx], test_case_list[j]
    for l in range(test_length):
        if test_case_list[l] == 0:
            test_case_list[l] = 'ZRO'
        elif test_case_list[l] == 1:
            test_case_list[l] = 'ONE'
        elif test_case_list[l] == 2:
            test_case_list[l] = 'TWO'
        elif test_case_list[l] == 3:
            test_case_list[l] = 'THR'
        elif test_case_list[l] == 4:
            test_case_list[l] = 'FOR'
        elif test_case_list[l] == 5:
            test_case_list[l] = 'FIV'
        elif test_case_list[l] == 6:
            test_case_list[l] = 'SIX'
        elif test_case_list[l] == 7:
            test_case_list[l] = 'SVN'
        elif test_case_list[l] == 8:
            test_case_list[l] = 'EGT'
        elif test_case_list[l] == 9:
            test_case_list[l] = 'NIN'


    print(f'{case_number}')
    print(*test_case_list)