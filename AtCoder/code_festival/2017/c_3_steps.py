n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [-1] * n

black = 0
white = 0

def dfs(v, c):
    global black, white
    
    color[v] = c
    if c == 0:
        black += 1
    else:
        white += 1

    for next_v in g[v]:
        if color[next_v] == c: 
            return False

        if color[next_v] == -1:
            if not dfs(next_v, 1 - c):
                return False
    return True

if dfs(0, 0):
    print(black * white - m)
else:
    print(n * (n - 1) // 2 - m)