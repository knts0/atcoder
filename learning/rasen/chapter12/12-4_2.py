# Breadth First Search

d = [-1] * 100

import queue
def bfs(u):
    q = queue.Queue()
    q.put(u)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if d[v] == -1:
                q.put(v)
                d[v] = d[u] + 1

n = int(input())

graph = [[] for i in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))
    
    u = lst[0]
    for v in lst[2:]:
        graph[u - 1].append(v - 1) # 0-originにする

d[0] = 0
bfs(0)

for u in range(n):
    print(str(u + 1) + " " + str(d[u]))