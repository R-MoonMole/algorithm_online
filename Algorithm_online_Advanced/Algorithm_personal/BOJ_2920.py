# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C,
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 시험 성적을 출력한다.
# 예제 100, 예제출력 A

# 백준 : 9498
# URL : https://www.acmicpc.net/problem/9498


a = input()

if a == '1 2 3 4 5 6 7 8':
    print('ascending')
elif a == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')