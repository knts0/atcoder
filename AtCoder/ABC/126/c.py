# result: https://atcoder.jp/contests/abc126/submissions/7212587

def calc_log2(x, y, cnt):
    if x >= y: return cnt
    return calc_log2(x * 2, y, cnt + 1)

def calc_power(num, acc):
    if num == 0: return acc
    else: return calc_power(num - 1, acc * 2)

n, k = list(map(int,input().split()))

max_log2 = calc_log2(1, k, 0)

li = [0] * n
molecure = 0
for i in range(n):
    li[i] = max_log2 - calc_log2(i + 1, k, 0)
    molecure += calc_power(li[i], 1)

denominator = n * max_log2

print(float(molecure) / denominator)
