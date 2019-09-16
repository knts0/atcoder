n, k, q = map(int, input().split())
cnt = [0] * n
for i in range(q):
    num = int(input())
    cnt[num - 1] += 1
for i in range(n):
    if k - (q - cnt[i]) > 0:
        print("Yes")
    else:
        print("No")