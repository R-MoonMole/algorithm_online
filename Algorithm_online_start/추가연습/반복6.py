data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

dic = {}

for i in data:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

print(dic)