# Depth First Search

visited = [False] * 100
d = [0] * 100
f = [0] * 100

time = 0

def dfs(u):
    if visited[u]:
        return
    else:
        # 初訪問
        visited[u] = True

        global time
        time += 1
        d[u] = time
 
        for v in graph[u]:
            dfs(v)
    
        time += 1
        f[u] = time

n = int(input())

graph = [[] for i in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))

    if lst[1] > 0:
        u = lst[0]
        for v in lst[2:]:
            graph[u - 1].append(v - 1) # 0-originにする

for u in range(n):
    dfs(u)

for u in range(n):
    print(str(u + 1) + " " + str(d[u]) + " " + str(f[u]))