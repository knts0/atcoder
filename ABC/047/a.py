l = sorted(map(int, input().split()))
print(type(l))
print("Yes" if l[0] + l[1] == l[2] else "No")