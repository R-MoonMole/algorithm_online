number = [7, 42, 5, 63, 111, 95]
answer = []
def solution(numbers):
    global answer

    for i in numbers:
        two_number = []
        result = True
        while i > 0:
            two_number.append(i % 2)
            i = i // 2
        if len(two_number) % 2 == 0:
            two_number.append(0)
        rev_two_number = two_number[::-1]
        rev_two_number.insert(0, 0)

        for j in range(1, len(rev_two_number)):
            if j % 2 == 0:
                if rev_two_number[j] == 0:
                    if rev_two_number[j-1] == rev_two_number[j+1] == 0:
                        continue
                    result = False
                    break
        if result == True:
            answer.append(1)
        elif result == False:
            answer.append(0)
    answer = answer[::-1]
    return answer

solution(number)
answer = answer[::-1]
print(answer)