lst = list(map(int, input().split()))
print("YES" if lst.count(5) == 2 and lst.count(7) == 1 else "NO")