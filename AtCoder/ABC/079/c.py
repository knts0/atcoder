# result: https://atcoder.jp/contests/abc079/submissions/7815188

ls = list(map(int, input()))

import sys
for bit in range(2 ** 3):
    sum = ls[0]
    ans = str(ls[0])
    for i in range(3):
        if bit >> i & 1:
            sum += ls[i + 1]
            ans += "+" + str(ls[i + 1])
        else:
            sum -= ls[i + 1]
            ans += "-" + str(ls[i + 1])
    if sum == 7:
        print(ans + "=7")
        sys.exit()