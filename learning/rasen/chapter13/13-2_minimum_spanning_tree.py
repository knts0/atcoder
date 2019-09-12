n = int(input())

INF = 1000000
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        graph[i][j] = lst[j] if lst[j] > 0 else INF

WHITE = 0
GRAY = 1
BLACK = 2
color = [WHITE] * n

d = [0] * n
p = [0] * n

def prim():
    ans = 0

    for i in range(n):
        color[i] = WHITE
        d[i] = INF
        p[i] = -1
    d[0] = 0

    while True:
        mincost = INF
        for i in range(n):
            if color[i] != BLACK and d[i] < mincost:
                mincost = d[i]
                u = i
        
        if mincost == INF:
            break
        else:
            ans += mincost
            
        color[u] = BLACK

        for v in range(n):
            if color[v] != BLACK and graph[u][v] > -1:
                if graph[u][v] < d[v]:
                    d[v] = graph[u][v]
                    p[v] = u
                    color[v] = GRAY
    
    return ans

print(prim())