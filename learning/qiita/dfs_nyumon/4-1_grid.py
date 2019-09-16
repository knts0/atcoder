h, w = map(int, input().split())

g = [['' for _ in range(w)] for _ in range(h)]

for i in range(h):
    g[i] = list(input())

si = 0
sj = 0
gi = 0
gj = 0

for i in range(h):
    for j in range(w):
        if g[i][j] == "s":
            si = i
            sj = j
        if g[i][j] == "g":
            gi = i
            gj = j

seen = [[False for _ in range(w)] for _ in range(h)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j):
    seen[i][j] = True

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue

        if seen[ni][nj]:
            continue
        
        if g[ni][nj] == "#":
            continue
        
        dfs(ni, nj)

dfs(si, sj)

if seen[gi][gj]:
    print("Yes")
else:
    print("No")