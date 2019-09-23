a, b = input().split()
if a == "H":
    print("H" if b == "H" else "D")
else:
    print("D" if b == "H" else "H")