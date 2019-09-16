n, m, s, t = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

seen = [False] * n

def dfs(v):
    seen[v] = True

    for next_v in g[v]:
        if not seen[next_v]: dfs(next_v)

dfs(s)

# tにたどり着ける場合Yes、そうでない場合Noを出力する
if seen[t]: print("Yes")
else: print("No")