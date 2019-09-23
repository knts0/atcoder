# result: https://atcoder.jp/contests/abc140/submissions/7425993

n, k = list(map(int,input().split()))
s = input()

init = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        init += 1

print(min(init + 2 * k, n - 1))
