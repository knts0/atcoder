n = int(input())

ans = 1
for i in range(n):
    ans = ans * (i + 1) % (10 ** 9 + 7)

print(ans)