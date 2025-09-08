import sys
sys.stdin = open("11806.txt", 'r')

T = int(input())

for tc in range(1, 1+T):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0

    def babygin(card_list, who):
        global winner, check
        card_list.sort()
        for i in range(len(card_list)-2):
            if card_list[i] == card_list[i+1] == card_list[i+2]:
                winner = who
        card_list = list(set(card_list))
        for j in range(len(card_list)-2):
            if card_list[j] == card_list[j+1]-1 == card_list[j+2]-2:
                winner = who

    for i in range(12):
        if i % 2 == 0:
            player1.append(arr[i])
            if len(player1) >= 3:
                babygin(player1, 1)
                if winner != 0:
                    break

        else:
            player2.append(arr[i])
            if len(player2) >= 3:
                babygin(player2, 2)
                if winner != 0:
                    break

    print(f'#{tc} {winner}')