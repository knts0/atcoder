# クラスカル法での閉路判定
n, m = map(int, input().split())

es = []

def kruskal():
    sorted(es, key=lambda x: x.cost)
    init_union_find(n) # Union-Findの初期化
    res = 0
    for i in range(m):
        e = es[i]
        if not same(e.u, e.v):
            unite(e.u, e.v)
            res +=e.cost
    
    return res
