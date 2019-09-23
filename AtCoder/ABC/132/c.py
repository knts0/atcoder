# result: https://atcoder.jp/contests/abc132/submissions/7312748

n = int(input())
d = list(map(int,input().split()))

d.sort()

if n % 2 == 0:
    if d[n // 2] == d[n // 2 + 1]:
        print(0)
    else:
        print(d[n // 2 + 1] - d[n // 2])
else:
    print(0)
