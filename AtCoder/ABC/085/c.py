# result: https://atcoder.jp/contests/abc085/submissions/7814588

import sys

n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n + 1):
        if 0 <= n - i - j <= n and i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(" ".join(map(str, [i, j, n - i - j])))
            sys.exit()
print("-1 -1 -1")