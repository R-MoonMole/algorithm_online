computer_number = int(input())
connect_number = int(input())
graph = [[] for _ in range(computer_number + 1)]
visited = [0] * (computer_number + 1)
result = []

for _ in range(connect_number):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def recur(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            recur(i)
            result.append(i)

recur(1)

print(result)
print(len(result))
