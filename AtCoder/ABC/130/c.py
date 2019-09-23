# result: https://atcoder.jp/contests/abc130/submissions/7235499

w, h, x, y = list(map(int,input().split()))

if w == x * 2 and h == y * 2:
    print(float(w) * h / 2, 1)
else:
    print(float(w) * h / 2, 0)
