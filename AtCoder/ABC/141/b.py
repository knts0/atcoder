s = input()
ans = True
for i in range(len(s)):
    if i % 2 == 0 and not s[i] in "RUD":
        ans = False
    elif i % 2 == 1 and not s[i] in "LUD":
        ans = False

print("Yes" if ans else "No")