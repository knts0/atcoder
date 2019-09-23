a, b, c = map(int, input().split())
l = sorted([abs(a - b), abs(b - c), abs(c - a)])
print(l[0] + l[1])