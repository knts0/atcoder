import math

d, g = map(int, input().split())
p = [0] * d
c = [0] * d
for i in range(d):
    p[i], c[i] = map(int, input().split())

ans = 10 ** 9
for bit in range(2 ** d):
    cnt = 0
    score = 0

    # ボーナス分の足し込み
    for i in range(d - 1, 0, -1):
        if bit >> i & 1 == 1:
            cnt += p[i]
            score += p[i] * (i + 1) * 100 + c[i]
    
    if score >= g:
        ans = min(ans, cnt)
    else:
        for i in range(d - 1, 0, -1):
            if bit >> i & 1 == 0:
                num = min(p[i] - 1, int(math.ceil((g - score) / (i + 1) * 100)))
                cnt += num
                score += num * (i + 1) * 100
            
            if score >= g:
                ans = min(ans, cnt)
                break

print(ans)