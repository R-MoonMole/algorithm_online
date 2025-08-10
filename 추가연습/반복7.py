data = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
want_data = []
result = 0

while len(data) > 0:

    if data[-1] > 80:
        want_data.append(data.pop())
    else:
        data.pop()

for i in want_data:
    result += i

print(result)