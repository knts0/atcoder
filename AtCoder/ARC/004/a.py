# result: https://atcoder.jp/contests/arc004/submissions/7814363

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(n):
        if i < j:
            ans = max(ans, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

print(ans ** (1 / 2))