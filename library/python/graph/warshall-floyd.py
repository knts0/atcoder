# 負の辺があっても動作する
n, m = map(int, input().split())

MAX_V = 10 ** 5
INF = 10 ** 9
d = [[INF] * MAX_V for _ in range(MAX_V)]

for i in range(m):
    a, b, w = map(int, input().split())
    d[a - 1][b - 1] = w
    d[b - 1][a - 1] = w

for i in range(n):
    d[i][i] = 0

def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][j] + d[k][j])