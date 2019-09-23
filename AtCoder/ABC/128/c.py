# result: https://atcoder.jp/contests/abc128/submissions/7234569

n, m = list(map(int,input().split()))

k = [0] * m
s = [[] for i in range(m)]
for i in range(m):
    ary = list(map(int,input().split()))
    k[i] = ary[0]
    s[i] = ary[1:]

p = list(map(int,input().split()))

ans = 0
for bit in range(2 ** n):
    on_light_cnt = 0
    for i in range(m):
        on_switch_cnt = 0
        for j in s[i]:
            if (bit >> (j - 1)) & 1 == 1:
                on_switch_cnt += 1

        if on_switch_cnt % 2 == p[i]:
            on_light_cnt += 1
    if on_light_cnt == m: ans += 1

print(ans)
