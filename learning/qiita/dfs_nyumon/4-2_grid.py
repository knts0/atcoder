import sys
for e in sys.stdin:

w, h = map(int, input().split())

if w == 0 or h == 0: sys.exit()

g = [["" for _ in range(w)] for _ in range(h)]

for i in range(h):
    g[i] = input().split()

di = [1, 0, -1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, 1, -1, 1, -1]

import queue
def dfs(i, j):
    g[i][j] = "0"

    q = queue.LifoQueue()
    q.put((i, j))

    while not q.empty():
        v = q.get()
        for k in range(8):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]

            if ni >= 0 and ni < h and nj >= 0 and nj < w:
                if g[ni][nj] == "1":
                    q.put((ni, nj))
                    g[ni][nj] = "0"

ans = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == "1":
            dfs(i, j)
            ans += 1

print(ans)