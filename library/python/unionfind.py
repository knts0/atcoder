par = []
rank = []

n = int(input())
par = [-1] * n   # 親ノード
rank = [0] * n

# 根を調べる
def root(x):
    if par[x] == -1:
        return x
    else: 
        par[x] = root(par[x])
        return par[x]

# 同じ集合に属するかチェック（同じ根になってるか）
def issame(x, y):
    return root(x) == root(y)

# 木の併合
def merge(x, y):
    x = root(x)
    y = root(y)
    if x == y: return False

    if rank[x] < rank[y]:
        x, y = y, x
    
    if rank[x] == rank[y]:
        rank[x] += 1
    
    par[y] = x
    return True