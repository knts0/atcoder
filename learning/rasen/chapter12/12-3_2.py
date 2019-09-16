n = int(input())

g = [[] for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    u = l[0]
    for j in l[2:]:
        g[u - 1].append(j - 1)

seen = [False] * n

d = [0] * n
f = [0] * n

t = 0

def dfs(v):
    seen[v] = True
    
    global t
    t += 1
    d[v] = t

    for next_v in g[v]:
        if not seen[next_v]: dfs(next_v)
    
    t += 1
    f[v] = t

dfs(0)

for i in range(n):
    print(str(i + 1) + " " + str(d[i]) + " " + str(f[i]))