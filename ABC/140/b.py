# result: https://atcoder.jp/contests/abc140/submissions/7405988

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = b[a[0] - 1]
for i in range(n - 1):
    ans += b[a[i + 1] - 1]
    if a[i] > 1 and a[i + 1] == a[i] + 1:
        ans += c[a[i + 1] - 1]

print(ans)
