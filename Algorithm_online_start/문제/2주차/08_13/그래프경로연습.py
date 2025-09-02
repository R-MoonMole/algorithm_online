'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

V, E = map(int, input().split())
arr = list(map(int,input().split()))

# G = [[0] * (V + 1) for _ in range(V + 1)] # 인접 행렬로 풀때
G = [[] for _ in range(V + 1)] # 인접 리스트로 풀때

for i in range (0, E*2, 2): # 0부터 16까지 2씩 건너뛰어서
    # arr[i], arr[i+1] 라고 바로써도 되는데 보기 좋으라구...;
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u) # 무향이기때문에 u->v, v->u 다 봐줌 유향이면 u->v만
    # 인접행렬이라면
    #G[u][v] = 1
    #G[v][u] = 1
# for i in range(1, V+1):
#     print (i, '-->', G[i])


# DFS를 위한 준비
# 1. 그래프 : G, 2. 스택 : S, 3. visited(방문정보)
S =[] # 스택 -> 빈 스택으로 만들면 while문에 True로 하면 되고, 아니면 출발점을 넣어서 시작
visited = [0] * (V + 1)

# 1. 시작 정점 v를 결정하여 방문한다.
v = 1 # 현재 위치한 정점
S.append(v)
visited[v] = 1; print(v, end=' ')
# 빈 스택이 아니면
while S:
    # 2. 정점 v에 인접한 정점 중에서 방문하지 않은 정점 w가 있으면, -> G[v]에서 w로 하나씩 가져오기
    for w in G[v]:
        if not visited[w]:
            # 2.1) 정점 v를 스택에 push하고 정점 w를 방문한다. -> v를 지나서 w로 감(v는 방문표시)
            # 그리고 w를 v로 하여 다시 2 를 반복한다.
            S.append(v)
            visited[w] = 1; print(w, end=' ')
            v = w
            break
    else: # 2.2) 방문하지 않은 정점이 없으면, 탐색의 방향을
        # 바꾸기 위해서 스택을 pop하여 받은 가장 마지막
        # 방문 정점을 v로 하여 다시 2 를 반복한다.
        v = S.pop()

# 3. 스택이 공백이 될 때까지 2. 를 반복한다.








