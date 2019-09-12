# connected components

n, m = list(map(int,input().split()))

graph = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b) # 0-originにする
    graph[b].append(a)

q = int(input())
questions = [[0, 0] for i in range(q)]
for i in range(q):
    a, b = list(map(int,input().split()))
    questions[i] = [a, b]

visited = [0] * 100000
def dfs(u, group):
    if visited[u] > 0:
        return
    else:
        # 初訪問
        visited[u] = group
 
        for v in graph[u]:
            dfs(v, group)

group = 0
for i in range(n):
    if visited[i] == 0:
        group += 1
        dfs(i, group)

for q in questions:
    if visited[q[0]] == visited[q[1]]:
        print('yes')
    else:
        print('no')