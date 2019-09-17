# 木DP
# ・各頂点の根からの距離（深さ）
# ・各頂点を根とした部分木のサイズ
n = int(input())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

depth = [0] * n
subtree_size = [0] * n

import queue
def dfs(v, p):
    for next_v in g[v]:
        if next_v == p:
            continue
        depth[next_v] = depth[v] + 1
        dfs(next_v, v)
    
    subtree_size[v] = 1
    for next_v in g[v]:
        if next_v == p:
            continue
        subtree_size[v] += subtree_size[next_v]

# 0を始点とする（親は-1）
dfs(0, -1)