s = input()

ans = 0
for bit in range(2 ** (len(s) - 1)):
    cnt = 0
    now = int(s[0])
    for i in range(len(s) - 1):
        if bit >> i & 1:
            cnt += now
            now = int(s[i + 1])
        else:
            now = now * 10 + int(s[i + 1])
    
    cnt += now
    ans += cnt

print(ans)