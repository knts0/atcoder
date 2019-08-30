# result: https://atcoder.jp/contests/abc127/submissions/7212807

import sys

n, m = list(map(int,input().split()))

overlap_l = 1
overlap_r = n
for i in range(m):
    l, r = list(map(int,input().split()))
    if overlap_r < l or r < overlap_l:
        print(0)
        sys.exit()
    else:
        overlap_l = max(l, overlap_l)
        overlap_r = min(r, overlap_r)

print(overlap_r - overlap_l + 1)
