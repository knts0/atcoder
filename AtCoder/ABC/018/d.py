n, m, p, q, r = map(int, input().split())

g = [[0] * m for _ in range(n)]

for i in range(r):
    x, y, z = map(int, input().split())
    g[x - 1][y - 1] = z

def next_combination(sub):
    x = sub & -sub
    y = sub + x
    return (((sub & ~y) // x) >> 1) | y

ans = 0

bit_p = (1 << p) - 1
while bit_p < (1 << n):

    sp = []
    for i in range(n):
        if bit_p & (1 << i):
            sp.append(i)
    
    
    bit_q = (1 << q) - 1
    while bit_q < (1 << m):
        cnt = 0

        sq = []
        for j in range(m):
            if bit_q & (1 << j):
                sq.append(j)
        
        bit_q = next_combination(bit_q)

        cnt = 0
        for i in sp:
            for j in sq:
                cnt += g[i][j]
        ans = max(cnt, ans)
        

    bit_p = next_combination(bit_p)

print(ans)